import appdirs
from pathlib import Path

from .client import Client
from .user_context import UserContext

config_dir = Path(appdirs.user_config_dir("recodex"))
data_dir = Path(appdirs.user_data_dir("recodex"))
context_path = data_dir / "context.yaml"

def get_client(api_url: str, username: str, password: str, verbose=False) -> Client:
    """Creates a client object. If the user context file is missing or expired,
    the file will be recreated using the provided credentials.
    
    Args:
        api_url (str): The URL of the API.
        username (str): ReCodEx username.
        password (str): ReCodEx password.
        verbose (bool, optional): Whether status messages should be printed to stdin. Defaults to False.

    Returns:
        Client: Returns a client object.
    """

    if not context_path.exists():
        user_context = __create_user_context(api_url, username, password, verbose)
    else:
        user_context = UserContext.load(context_path)
        if user_context.is_token_expired:
            user_context = __create_user_context(api_url, username, password, verbose)

    return get_client_from_user_context(user_context)

def get_client_from_user_context(user_context: UserContext) -> Client:
    """Creates a client object and refreshes the API token if it almost expired.

    Args:
        user_context (UserContext): The user context containing the endpoint URL and API token.

    Returns:
        Client: Returns a client object.
    """

    client = Client(user_context.api_token, user_context.api_url)

    # refresh token if necessary
    if user_context.is_token_almost_expired():
        user_context = user_context.replace_token(client.get_refresh_token())
        user_context.store(context_path)
        # recreate client
        client = Client(user_context.api_token, user_context.api_url)
    return client

def load_user_context() -> UserContext | None:
    """Creates a UserContext object from a file if it exists.

    Returns:
        (UserContext | None): Returns the loaded UserContext, or None if there is no file.
    """

    if not context_path.exists():
        return None
    return UserContext.load(context_path)

def __create_user_context(api_url: str, username: str, password: str, verbose=False) -> UserContext:
    """Retrieves an API token and creates a user context file from the provided credentials.

    Args:
        api_url (str): The URL of the API.
        username (str): ReCodEx username.
        password (str): ReCodEx password.
        verbose (bool, optional): Whether status messages should be printed to stdin. Defaults to False.

    Returns:
        UserContext: Returns a user context object used to create a client object.
    """

    client = Client("", api_url)
    
    if verbose:
        print("Connecting...")
    token = client.get_login_token(username, password)
    user_context = UserContext(api_url, token)

    user_context.store(context_path)
    if verbose:
        print(f"Login token stored at: {context_path}")

    return user_context
