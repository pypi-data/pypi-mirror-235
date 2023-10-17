"""Utility functions for getting or creating user accounts
"""

from typing import Any, Dict, Optional, Tuple, Union

from dictor import dictor  # type: ignore
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, User
from django_saml2_auth.errors import (
    CREATE_USER_ERROR,
    GROUP_JOIN_ERROR,
    SHOULD_NOT_CREATE_USER,
)
from django_saml2_auth.exceptions import SAMLAuthError
from django_saml2_auth.utils import run_hook


def create_new_user(
    email: str,
    first_name: Optional[str] = None,
    last_name: Optional[str] = None,
    **kwargs,
) -> User:
    """Create a new user with the given information

    Args:
        email (str): Email
        first_name (str): First name
        last_name (str): Last name

    Keyword Args:
        **kwargs: Additional keyword arguments

    Raises:
        SAMLAuthError: There was an error creating the new user.
        SAMLAuthError: There was an error joining the user to the group.

    Returns:
        User: Returns a new user object, usually a subclass of the the User model
    """
    saml2_auth_settings = settings.SAML2_AUTH
    user_model = get_user_model()

    is_active = dictor(
        saml2_auth_settings, "NEW_USER_PROFILE.ACTIVE_STATUS", default=True
    )
    is_staff = dictor(
        saml2_auth_settings, "NEW_USER_PROFILE.STAFF_STATUS", default=False
    )
    is_superuser = dictor(
        saml2_auth_settings, "NEW_USER_PROFILE.SUPERUSER_STATUS", default=False
    )
    user_groups = dictor(
        saml2_auth_settings, "NEW_USER_PROFILE.USER_GROUPS", default=[]
    )

    if first_name and last_name:
        kwargs["first_name"] = first_name
        kwargs["last_name"] = last_name

    try:
        user = user_model.objects.create_user(email, **kwargs)
        user.is_active = is_active
        user.is_staff = is_staff
        user.is_superuser = is_superuser
        user.save()
    except Exception as exc:
        raise SAMLAuthError(
            "There was an error creating the new user.",
            extra={
                "exc": exc,
                "exc_type": type(exc),
                "error_code": CREATE_USER_ERROR,
                "reason": "There was an error processing your request.",
                "status_code": 500,
            },
        )

    try:
        groups = [Group.objects.get(name=group) for group in user_groups]
        if groups:
            user.groups.set(groups)
    except Exception as exc:
        raise SAMLAuthError(
            "There was an error joining the user to the group.",
            extra={
                "exc": exc,
                "exc_type": type(exc),
                "error_code": GROUP_JOIN_ERROR,
                "reason": "There was an error processing your request.",
                "status_code": 500,
            },
        )

    user.save()
    user.refresh_from_db()

    return user


def get_or_create_user(user: Dict[str, Any]) -> Tuple[bool, User]:
    """Get or create a new user and optionally add it to one or more group(s)

    Args:
        user (Dict[str, Any]): User information

    Raises:
        SAMLAuthError: Cannot create user. Missing user_id.
        SAMLAuthError: Cannot create user.

    Returns:
        Tuple[bool, User]: A tuple containing user creation status and user object
    """
    saml2_auth_settings = settings.SAML2_AUTH
    user_model = get_user_model()
    created = False

    try:
        target_user = get_user(user)
    except user_model.DoesNotExist:
        should_create_new_user = dictor(saml2_auth_settings, "CREATE_USER", True)
        if should_create_new_user:
            user_id = get_user_id(user)
            if not user_id:
                raise SAMLAuthError(
                    "Cannot create user. Missing user_id.",
                    extra={
                        "error_code": SHOULD_NOT_CREATE_USER,
                        "reason": "Cannot create user. Missing user_id.",
                        "status_code": 400,
                    },
                )
            target_user = create_new_user(
                user_id, user["first_name"], user["last_name"]
            )

            create_user_trigger = dictor(saml2_auth_settings, "TRIGGER.CREATE_USER")
            if create_user_trigger:
                run_hook(create_user_trigger, user)  # type: ignore

            target_user.refresh_from_db()
            created = True
        else:
            raise SAMLAuthError(
                "Cannot create user.",
                extra={
                    "exc_type": Exception,
                    "error_code": SHOULD_NOT_CREATE_USER,
                    "reason": "Due to current config, a new user should not be created.",
                    "status_code": 500,
                },
            )

    # Optionally update this user's group assignments by updating group memberships from SAML groups
    # to Django equivalents
    group_attribute = dictor(saml2_auth_settings, "ATTRIBUTES_MAP.groups")
    group_map = dictor(saml2_auth_settings, "GROUPS_MAP")

    if group_attribute and group_attribute in user["user_identity"]:
        groups = []

        for group_name in user["user_identity"][group_attribute]:
            # Group names can optionally be mapped to different names in Django
            if group_map and group_name in group_map:
                group_name_django = group_map[group_name]
            else:
                group_name_django = group_name

            group = Group.objects.filter(name=group_name_django).first()
            if group:
                groups.append(Group.objects.get(name=group_name_django))
            else:
                should_create_new_groups = dictor(
                    saml2_auth_settings, "CREATE_GROUPS", False
                )
                if should_create_new_groups:
                    groups.append(Group.objects.create(name=group_name_django))

        target_user.groups.set(groups)

    return (created, target_user)


def get_user_id(user: Union[str, Dict[str, Any]]) -> Optional[str]:
    """Get user_id (username or email) from user object

    Args:
        user (Union[str, Dict[str, Any]]): A cleaned user info object

    Returns:
        Optional[str]: user_id, which is either email or username
    """
    user_model = get_user_model()
    user_id = None

    if isinstance(user, dict):
        user_id = (
            user["email"] if user_model.USERNAME_FIELD == "email" else user["username"]
        )

    if isinstance(user, str):
        user_id = user

    return user_id.lower() if user_id else None


def get_user(user: Union[str, Dict[str, str]]) -> User:
    """Get user from database given a cleaned user info object or a user_id

    Args:
        user (Union[str, Dict[str, str]]): Either a user_id (as str) or a cleaned user info object

    Returns:
        User: An instance of the User model
    """
    saml2_auth_settings = settings.SAML2_AUTH
    get_user_custom_method = dictor(saml2_auth_settings, "TRIGGER.GET_USER")

    user_model = get_user_model()
    if get_user_custom_method:
        found_user = run_hook(get_user_custom_method, user)  # type: ignore
        if not found_user:
            raise user_model.DoesNotExist
        else:
            return found_user

    user_id = get_user_id(user)

    # Should email be case-sensitive or not. Default is False (case-insensitive).
    login_case_sensitive = dictor(saml2_auth_settings, "LOGIN_CASE_SENSITIVE", False)
    id_field = (
        user_model.USERNAME_FIELD
        if login_case_sensitive
        else f"{user_model.USERNAME_FIELD}__iexact"
    )
    return user_model.objects.get(**{id_field: user_id})


def create_custom_or_default_jwt(user: Union[str, User]):
    """Create a new JWT token, eventually using custom trigger

    Args:
        user (Union[str, User]): User instance or User's username or email
            based on User.USERNAME_FIELD

    Raises:
        SAMLAuthError: Cannot create JWT token. Specify a user.

    Returns:
        Optional[str]: JWT token
    """
    saml2_auth_settings = settings.SAML2_AUTH
    user_model = get_user_model()

    custom_create_jwt_trigger = dictor(saml2_auth_settings, "TRIGGER.CUSTOM_CREATE_JWT")

    # If user is the id (user_model.USERNAME_FIELD), set it as user_id
    user_id: Optional[str] = None
    if isinstance(user, str):
        user_id = user

    # Check if there is a custom trigger for creating the JWT and URL query
    if custom_create_jwt_trigger:
        target_user = user
        # If user is user_id, get user instance
        if user_id:
            user_model = get_user_model()
            _user = {user_model.USERNAME_FIELD: user_id}
            target_user = get_user(_user)
        return run_hook(custom_create_jwt_trigger, target_user)  # type: ignore
    raise SAMLAuthError("You must specify TRIGGER.CUSTOM_CREATE_JWT.")


def decode_custom_or_default_jwt(jwt_token: str) -> Optional[str]:
    """Decode a JWT token, eventually using custom trigger

    Args:
        jwt_token (str): The token to decode

    Raises:
        SAMLAuthError: Cannot decode JWT token.

    Returns:
        Optional[str]: A user_id as str or None.
    """
    saml2_auth_settings = settings.SAML2_AUTH
    custom_decode_jwt_trigger = dictor(saml2_auth_settings, "TRIGGER.CUSTOM_DECODE_JWT")
    if custom_decode_jwt_trigger:
        return run_hook(custom_decode_jwt_trigger, jwt_token)  # type: ignore
    raise SAMLAuthError("You must specify TRIGGER.CUSTOM_DECODE_JWT.")
