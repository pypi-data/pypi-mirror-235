from getpass import getpass
from os import environ
from time import time
from typing import Union

import requests

CLOCK_SKEW_SECONDS = 5 * 60
token_cache = {}


def ensure_list(value: Union[list[str], str]) -> list[str]:
    """
    Helper function that always returns a string as a list[str].

    """

    return [value] if isinstance(value, str) else value


def get_config() -> tuple[str]:
    """
    Returns a tuple with variables for connecting to the Azure AD client.

    Attempts to read AAD_TENANT_ID, AAD_CLIENT_ID and AAD_CLIENT_SECRET
    from settings.py when running from Django, or alternatively from os.environ
    if Django is not installed or settings are not initialized.

    Prompts the user for input if any of the required variables are empty.

    """

    try:
        from django.conf import settings

        # If settings.py is initialized
        if settings.configured:
            tenant_id = settings.AAD_TENANT_ID
            client_id = settings.AAD_CLIENT_ID
            client_secret = settings.AAD_CLIENT_SECRET
        else:
            raise ImportError("Django not running")

    # Django is not installed or not running
    except ImportError:
        tenant_id = environ.get("AAD_TENANT_ID")
        client_id = environ.get("AAD_CLIENT_ID")
        client_secret = environ.get("AAD_CLIENT_SECRET")

    if not tenant_id:
        tenant_id = input("AAD_TENANT_ID: ")
    if not client_id:
        client_id = input("AAD_CLIENT_ID: ")
    if not client_secret:
        client_secret = getpass("AAD_CLIENT_SECRET: ")

    return (
        tenant_id,
        client_id,
        client_secret,
    )


def get_token() -> str:
    """
    Returns an access token for the client in Azure AD.
    Uses the same token from token_cache in repeated API-calls.

    Documentation:
    https://learn.microsoft.com/en-us/graph/auth/auth-concepts

    """

    global token_cache
    if token_cache:
        if token_cache["exp"] >= time() + CLOCK_SKEW_SECONDS:
            return token_cache["jwt"]

    (tenant_id, client_id, client_secret) = get_config()

    response = requests.post(
        url=f"https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token",
        data={
            "grant_type": "client_credentials",
            "scope": "https://graph.microsoft.com/.default",
            "client_id": client_id,
            "client_secret": client_secret,
        },
    )
    if response.status_code != 200:
        error_message = response.json().get("error_description")
        raise ConnectionError(
            f"Request failed ({response.status_code} {response.reason}):\n"
            f"{error_message}"
        )
    response = response.json()
    token_cache["jwt"] = response["access_token"]
    token_cache["exp"] = time() + response["expires_in"]

    return response["access_token"]


def clear_cache():
    global token_cache
    if token_cache:
        del token_cache
