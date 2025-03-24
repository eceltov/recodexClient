import os
import yaml
from .utils import camel_case_to_snake_case
from prance import ResolvingParser
from .generated.swagger_client import ApiClient
from .generated.swagger_client.rest import ApiException
from .alias_container import AliasContainer

class EndpointResolver:
    def __init__(self, generated_api):
        self.generated_api: ApiClient = generated_api

        # load aliases.yaml
        self.__load_user_aliases()

        # load the swagger spec
        self.__load_spec()

        # extract endpoint definitions
        self.__init_definitions()

        # init the alias container and add user aliases
        self.__init_aliases()        

    def __load_spec(self):
        # the swagger is located in the 'generated' folder
        dirname = os.path.dirname(__file__)
        filepath = os.path.join(dirname, 'generated/swagger.yaml')
        parser = ResolvingParser(filepath, backend='openapi-spec-validator')
        self.spec = parser.specification


    def __load_user_aliases(self):
        dirname = os.path.dirname(__file__)
        filepath = os.path.join(dirname, 'aliases.yaml')
        with open(filepath) as file:
            self.user_aliases: dict[str, dict] = yaml.safe_load(file)

    # construct dict from operationId (snake case) to endpoint definitions
    # definitions are identical to swagger definitions (body of method field) with the added 'method' key
    def __init_definitions(self):
        self.definitions: dict[str, dict] = {}
        for path, path_body in self.spec["paths"].items():
            for method, method_body in path_body.items():
                method_body["method"] = method
                operation_id = method_body["operationId"]
                snake_case_operation_id = camel_case_to_snake_case(operation_id)
                self.definitions[snake_case_operation_id] = method_body

    def __init_aliases(self):
        # init the alias container
        self.alias_container = AliasContainer(self.definitions)

        for presenter, presenter_alias_obj in self.user_aliases.items():
            if 'alias' in presenter_alias_obj:
                self.alias_container.add_presenter_alias(presenter, presenter_alias_obj['alias'])

            if 'endpoints' not in presenter_alias_obj:
                continue

            for endpoint, endpoint_alias in presenter_alias_obj['endpoints'].items():
                self.alias_container.add_endpoint_alias(presenter, endpoint, endpoint_alias)

    def get_endpoint_callback(self, presenter, endpoint):
        operation_id = self.alias_container.get_operation_id(presenter, endpoint)
        endpoint_callback = getattr(self.generated_api, operation_id, None)
        if endpoint_callback == None:
            raise ApiException(500, f"Endpoint {operation_id} not found.")
        return endpoint_callback

    def get_endpoint_definition(self, presenter, endpoint):
        operation_id = self.alias_container.get_operation_id(presenter, endpoint)
        return self.definitions[operation_id]
