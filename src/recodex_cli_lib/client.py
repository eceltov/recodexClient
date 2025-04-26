import json
from .generated.swagger_client import ApiClient
from .generated.swagger_client import DefaultApi
from .generated.swagger_client.configuration import Configuration
from .generated.swagger_client.rest import ApiException
from .generated.swagger_client.rest import RESTResponse
from .swagger_validator import SwaggerValidator
from .endpoint_resolver import EndpointResolver

class Client:
    def __init__(self, token, host):
        config = Configuration()
        config.host = host
        self.generated_client = ApiClient(config, "Authorization", f"Bearer {token}")
        self.generated_api = DefaultApi(self.generated_client)
        self.endpoint_resolver = EndpointResolver(self.generated_api)
        self.validator = SwaggerValidator(self.endpoint_resolver)

    # converts boolean values of the dict to 'true' or 'false'
    # the urllib.urlencode function used converts bools to 'True' or 'False', which causes an error on the endpoint
    def fix_boolean_url_params(self, params: dict):
        for key, value in params.items():
            if value == True or value == False:
                params[key] = str(value).lower()

    def get_login_token(self, username, password):
        response = self.send_request("login", "default", {
            "username": username,
            "password": password,
        })
        response_dict = json.loads(response.data.decode("utf-8"))
        return response_dict["payload"]["accessToken"]

    def get_refresh_token(self):
        response = self.send_request("login", "refresh")
        response_dict = json.loads(response.data.decode("utf-8"))
        return response_dict["payload"]["accessToken"]

    def send_request(self, presenter, handler, body={}, path_params={}, query_params={}):
        endpoint_callback = self.endpoint_resolver.get_endpoint_callback(presenter, handler)

        # validate the request (throws jsonschema.exceptions.ValidationError when invalid)
        self.validator.validate(presenter, handler, body, path_params, query_params)

        # convert boolean values to strings to avoid urllib errors
        self.fix_boolean_url_params(path_params)
        self.fix_boolean_url_params(query_params)

        # the endpoints must not have the body param passed if empty
        if bool(body):
            endpoint_callback(body=body, **path_params, **query_params)
        else:
            endpoint_callback(**path_params, **query_params)

        response: RESTResponse = self.generated_client.last_response
        return response
