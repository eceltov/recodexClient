from src.recodex_cli_lib.client import Client

token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL3lvdXIucmVjb2RleC5kb21haW4iLCJhdWQiOiJodHRwczovL3lvdXIucmVjb2RleC5kb21haW4iLCJpYXQiOjE3NDQ4OTQ5MTcsIm5iZiI6MTc0NDg5NDkxNywiZXhwIjoxNzQ1NDk5NzE3LCJzdWIiOiJiNjA1MGFhNC1mODExLTQxMDItYWU4NC0wN2MzOTAwNmFkNWMiLCJlZmZyb2xlIjpudWxsLCJzY29wZXMiOlsibWFzdGVyIiwicmVmcmVzaCJdfQ.xx5z3Lnq2oCCfbhMdT2XL2_MsDV2dfQbyp4iQXhJPfk"
host = "http://localhost:4000"

client = Client(token, host)

body = {
    "a": "tes",
    "d": 7.1,
    "e": False
}

path_params = { "param":"1" }
query_params = { "b": True, "c": 5.5 }

response = client.send_request('reg', 'dbg', body, path_params, query_params)
print(response.data)
