from __future__ import print_function
import time
# import src.generated.swagger_client as swagger_client
# from src.client import Client

from src.recodex_cli_lib.client import Client
from src.recodex_cli_lib.swagger_validator import SwaggerValidator

# import swagger_client
from src.recodex_cli_lib.generated.swagger_client.rest import ApiException
from src.recodex_cli_lib.generated.swagger_client.configuration import Configuration
from src.recodex_cli_lib.generated.swagger_client.rest import RESTResponse
from src.recodex_cli_lib.generated.swagger_client import DebugParamBody
# from client import Client

# print(definition)

# object_methods = [method_name for method_name in dir(validator)
#   if callable(getattr(validator, method_name))]
# print(object_methods)

token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL3lvdXIucmVjb2RleC5kb21haW4iLCJhdWQiOiJodHRwczovL3lvdXIucmVjb2RleC5kb21haW4iLCJpYXQiOjE3NDE4NzE3NzEsIm5iZiI6MTc0MTg3MTc3MSwiZXhwIjoxNzQyNDc2NTcxLCJzdWIiOiJiNjA1MGFhNC1mODExLTQxMDItYWU4NC0wN2MzOTAwNmFkNWMiLCJlZmZyb2xlIjpudWxsLCJzY29wZXMiOlsibWFzdGVyIiwicmVmcmVzaCJdfQ.9rQYUhZmeze2CpuZ12pDt1xM3WlompU1Gvxiiyd0c_E"
host = "http://localhost:4000"

client = Client(token, host)

body = DebugParamBody(
    a="tes",
    d=7.1
)

path_params = { "param":"1" }
query_params = { "b": False, "c": 5.5 }

response = client.send_request("registration_debug", body, path_params, query_params)
print(response.data)
