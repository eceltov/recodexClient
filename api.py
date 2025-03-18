from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from swagger_client.configuration import Configuration
from swagger_client.rest import RESTResponse
from client import Client

token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL3lvdXIucmVjb2RleC5kb21haW4iLCJhdWQiOiJodHRwczovL3lvdXIucmVjb2RleC5kb21haW4iLCJpYXQiOjE3NDE4NzE3NzEsIm5iZiI6MTc0MTg3MTc3MSwiZXhwIjoxNzQyNDc2NTcxLCJzdWIiOiJiNjA1MGFhNC1mODExLTQxMDItYWU4NC0wN2MzOTAwNmFkNWMiLCJlZmZyb2xlIjpudWxsLCJzY29wZXMiOlsibWFzdGVyIiwicmVmcmVzaCJdfQ.9rQYUhZmeze2CpuZ12pDt1xM3WlompU1Gvxiiyd0c_E"
host = "http://localhost:4000"

client = Client(token, host)

body = swagger_client.DebugParamBody(
    a="test@test.test",
)

response = client.send_request("registration_debug", body, path_query_params={"param":"1", "b":"false"})
print(response.data)
