from __future__ import print_function
from .generated.swagger_client import ApiClient
from .generated.swagger_client import DefaultApi
from .generated.swagger_client.configuration import Configuration
from .generated.swagger_client.rest import ApiException
from .generated.swagger_client.rest import RESTResponse

class Client:
    def __init__(self, token, host):
        config = Configuration()
        config.host = host
        self.generated_client = ApiClient(config, "Authorization", f"Bearer {token}")
        self.api = DefaultApi(self.generated_client)

    def send_request(self, endpoint_id, body=None, path_query_params={}):
        endpoint = getattr(self.api, endpoint_id, None)
        if endpoint == None:
            raise ApiException(500, f"Endpoint {endpoint_id} not found.")

        endpoint(body=body, **path_query_params)
        response: RESTResponse = self.generated_client.last_response
        return response
