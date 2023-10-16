from getpass import getpass
from os import environ


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
