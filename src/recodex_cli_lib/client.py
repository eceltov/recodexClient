import json
from collections.abc import Callable

from .generated.swagger_client import ApiClient
from .generated.swagger_client import DefaultApi
from .generated.swagger_client.configuration import Configuration
from .generated.swagger_client.rest import ApiException
from .generated.swagger_client.rest import RESTResponse
from .swagger_validator import SwaggerValidator
from .endpoint_resolver import EndpointResolver
from .client_response import ClientResponse
from .utils import parse_endpoint_function

class Client:
    def __init__(self, token, host):
        config = Configuration()
        config.host = host
        self.generated_client = ApiClient(config, "Authorization", f"Bearer {token}")
        self.generated_api = DefaultApi(self.generated_client)
        self.endpoint_resolver = EndpointResolver()
        self.validator = SwaggerValidator()

    # converts boolean values of the dict to 'true' or 'false'
    # the urllib.urlencode function used converts bools to 'True' or 'False', which causes an error on the endpoint
    def __fix_boolean_url_params(self, params: dict):
        for key, value in params.items():
            if value == True or value == False:
                params[key] = str(value).lower()

    def get_login_token(self, username: str, password: str):
        response = self.send_request("login", "default", {
            "username": username,
            "password": password,
        })
        response_dict = response.get_parsed_data()
        return response_dict["payload"]["accessToken"]

    def get_refresh_token(self):
        response = self.send_request("login", "refresh")
        response_dict = response.get_parsed_data()
        return response_dict["payload"]["accessToken"]

    def send_request(self, presenter: str, handler: str, body={}, path_params={}, query_params={}, files={}, raw_body=False) -> ClientResponse:
        endpoint_definition = self.endpoint_resolver.get_endpoint_definition(presenter, handler)

        if raw_body:
            self.validator.validate(endpoint_definition, path_params=path_params, query_params=query_params)
        else:
            # validate the request (throws jsonschema.exceptions.ValidationError when invalid)
            self.validator.validate(endpoint_definition, body, path_params, query_params)

        # convert boolean values to strings to avoid urllib errors
        self.__fix_boolean_url_params(path_params)
        self.__fix_boolean_url_params(query_params)

        endpoint_callback = self.endpoint_resolver.get_endpoint_callback(presenter, handler, self.generated_api)

        # the endpoints must not have the body param passed if empty
        if bool(body):
            endpoint_callback(body=body, **path_params, **query_params, **files)
        else:
            endpoint_callback(**path_params, **query_params, **files)

        raw_response: RESTResponse = self.generated_client.last_response
        response = ClientResponse(raw_response)

        return response

    def send_request_by_callback(self, endpoint: Callable, body={}, path_params={}, query_params={}, files={}, raw_body=False) -> ClientResponse:
        presenter, handler = parse_endpoint_function(endpoint)
        self.send_request(presenter, handler, body, path_params, query_params, files, raw_body)
