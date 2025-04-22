import appdirs
from pathlib import Path
from config import UserContext

from src.recodex_cli_lib.client import Client

config_dir = Path(appdirs.user_config_dir("recodex"))
data_dir = Path(appdirs.user_data_dir("recodex"))
context_path = data_dir / "context.yaml"

if not context_path.exists():
    api_url = input("API URL:  ")
    username = input("Username: ")
    password = input("Password: ")
    client = Client("", api_url)
    token = client.get_login_token(username, password)
    user_context = UserContext(api_url, token)
    user_context.store(context_path)

# user_context = UserContext.load(
#     context_path) if context_path.exists() else UserContext()
# api_client = Client(user_context.api_token, user_context.api_url)

# if user_context.api_token is not None and user_context.is_token_almost_expired() and not user_context.is_token_expired:
#     user_context = user_context.replace_token(api_client.get_refresh_token())
#     user_context.store(context_path)


# token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL3lvdXIucmVjb2RleC5kb21haW4iLCJhdWQiOiJodHRwczovL3lvdXIucmVjb2RleC5kb21haW4iLCJpYXQiOjE3NDQ4OTQ5MTcsIm5iZiI6MTc0NDg5NDkxNywiZXhwIjoxNzQ1NDk5NzE3LCJzdWIiOiJiNjA1MGFhNC1mODExLTQxMDItYWU4NC0wN2MzOTAwNmFkNWMiLCJlZmZyb2xlIjpudWxsLCJzY29wZXMiOlsibWFzdGVyIiwicmVmcmVzaCJdfQ.xx5z3Lnq2oCCfbhMdT2XL2_MsDV2dfQbyp4iQXhJPfk"
# host = "http://localhost:4000"

# client = Client(token, host)
# print(client.get_login_token("kliber@d3s.mff.cuni.cz", "heslo"))

# print(client.get_refresh_token())

# body = {
#     "a": "tes",
#     "d": 7.1,
#     "e": False
# }

# path_params = { "param":"1" }
# query_params = { "b": True, "c": 5.5 }

# response = client.send_request('reg', 'dbg', body, path_params, query_params)
# print(response.data)
