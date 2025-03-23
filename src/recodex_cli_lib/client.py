from __future__ import print_function
from .generated.swagger_client import ApiClient
from .generated.swagger_client import DefaultApi
from .generated.swagger_client.configuration import Configuration
from .generated.swagger_client.rest import ApiException
from .generated.swagger_client.rest import RESTResponse
from .swagger_validator import SwaggerValidator

class Client:
    def __init__(self, token, host):
        config = Configuration()
        config.host = host
        self.generated_client = ApiClient(config, "Authorization", f"Bearer {token}")
        self.api = DefaultApi(self.generated_client)
        self.validator = SwaggerValidator()

    def send_request(self, operation_id, body={}, path_params={}, query_params={}):
        endpoint = getattr(self.api, operation_id, None)
        if endpoint == None:
            raise ApiException(500, f"Endpoint {operation_id} not found.")

        # validate the request (throws jsonschema.exceptions.ValidationError when invalid)
        self.validator.validate(operation_id, body, path_params, query_params)

        endpoint(body=body, **path_params, **query_params)
        response: RESTResponse = self.generated_client.last_response
        return response
