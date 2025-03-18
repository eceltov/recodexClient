from __future__ import print_function
import swagger_client
from swagger_client.configuration import Configuration
from swagger_client.rest import ApiException
from swagger_client.rest import RESTResponse

class Client:
    def __init__(self, token, host):
        config = Configuration()
        config.host = host
        self.generated_client = swagger_client.ApiClient(config, "Authorization", f"Bearer {token}")
        self.api = swagger_client.DefaultApi(self.generated_client)

    def send_request(self, endpoint_id, body=None, path_query_params={}):
        endpoint = getattr(self.api, endpoint_id, None)
        if endpoint == None:
            raise ApiException(500, f"Endpoint {endpoint_id} not found.")

        endpoint(body=body, **path_query_params)
        response: RESTResponse = self.generated_client.last_response
        return response
