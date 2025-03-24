from __future__ import print_function
from .generated.swagger_client import ApiClient
from .generated.swagger_client import DefaultApi
from .generated.swagger_client.configuration import Configuration
from .generated.swagger_client.rest import ApiException
from .generated.swagger_client.rest import RESTResponse
from .swagger_validator import SwaggerValidator
from.endpoint_resolver import EndpointResolver

class Client:
    def __init__(self, token, host):
        config = Configuration()
        config.host = host
        self.generated_client = ApiClient(config, "Authorization", f"Bearer {token}")
        self.generated_api = DefaultApi(self.generated_client)
        self.endpoint_resolver = EndpointResolver(self.generated_api)
        self.validator = SwaggerValidator(self.endpoint_resolver)

    def send_request(self, presenter, endpoint, body={}, path_params={}, query_params={}):
        endpoint_callback = self.endpoint_resolver.get_endpoint_callback(presenter, endpoint)

        # validate the request (throws jsonschema.exceptions.ValidationError when invalid)
        self.validator.validate(presenter, endpoint, body, path_params, query_params)

        endpoint_callback(body=body, **path_params, **query_params)
        response: RESTResponse = self.generated_client.last_response
        return response
