import appdirs
from pathlib import Path
import typer

from .client import Client
from .userContext import UserContext

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

    return __create_client(user_context)

def get_client_interactive() -> Client:
    """Creates a client object. If the user context file is missing or expired,
    prompts the user via CLI for login credentials.

    Returns:
        Client: Returns a client object.
    """

    # show log in prompt if there is no session
    if not context_path.exists():
        user_context = __login()
    # load session data
    else:
        user_context = UserContext.load(context_path)
        if user_context.is_token_expired:
            typer.echo("Token is expired, please log in to continue.")
            # use the old API url
            user_context = __prompt_user_context(user_context.api_url)

    return __create_client(user_context)

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
        typer.echo("Connecting...")
    token = client.__get_login_token(username, password)
    user_context = UserContext(api_url, token)

    user_context.store(context_path)
    if verbose:
        typer.echo(f"Login token stored at: {context_path}")

    return user_context

def __create_client(user_context: UserContext) -> Client:
    """Creates a client object and refreshes the API token if it almost expired.

    Args:
        user_context (UserContext): The user context containing the endpoint URL and API token.

    Returns:
        Client: Returns a client object.
    """

    client = Client(user_context.api_token, user_context.api_url)

    # refresh token if necessary
    if user_context.is_token_almost_expired():
        user_context = user_context.replace_token(client.__get_refresh_token())
        user_context.store(context_path)
        # recreate client
        client = Client(user_context.api_token, user_context.api_url)
    return client

def __prompt_user_context(api_url) -> UserContext:
    username = typer.prompt("Username")
    password = typer.prompt("Password", hide_input=True)
    return __create_user_context(api_url, username, password, verbose=True)

def __login() -> UserContext:
    api_url = typer.prompt("API URL")
    return __prompt_user_context(api_url)
