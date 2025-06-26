import os
import yaml
from prance import ResolvingParser
from .utils import camel_case_to_snake_case
from .generated.openapi_client import ApiClient
from .generated.openapi_client.rest import ApiException
from .alias_container import AliasContainer

class EndpointResolver:
    def __init__(self):
        # load aliases.yaml
        self.__load_user_aliases()

        # load the swagger spec
        self.__load_spec()

        # extract endpoint definitions
        self.__init_definitions()

        # init the alias container and add user aliases
        self.__init_aliases()        

    def __get_spec_path(self):
        # the swagger is located in the 'generated' folder
        dirname = os.path.dirname(__file__)
        return os.path.join(dirname, 'generated/swagger.yaml')

    def __load_spec(self):
        filepath = self.__get_spec_path()
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

                # add snake case names used by the endpoint functions                
                if "parameters" in method_body:
                    param_defs = method_body["parameters"]
                    for param_def in param_defs:
                        param_def["python_name"] = camel_case_to_snake_case(param_def["name"])

                operation_id = method_body["operationId"]
                snake_case_operation_id = camel_case_to_snake_case(operation_id)
                self.definitions[snake_case_operation_id] = method_body

    def __init_aliases(self):
        # init the alias container
        self.alias_container = AliasContainer(self.definitions)

        for presenter, presenter_alias_obj in self.user_aliases.items():
            if 'alias' in presenter_alias_obj:
                self.alias_container.add_presenter_alias(presenter, presenter_alias_obj['alias'])

            if 'handlers' not in presenter_alias_obj:
                continue

            for handler, handler_alias in presenter_alias_obj['handlers'].items():
                self.alias_container.add_handler_alias(presenter, handler, handler_alias)

    def get_swagger(self) -> str:
        """Reads the current swagger specification file and returns it.

        Returns:
            str: Returns the content of the swagger specification file.
        """
        filepath = self.__get_spec_path()
        with open(filepath, "r") as handle:
            return handle.read()

    def get_endpoint_callback(self, presenter: str, handler: str, generated_api: ApiClient):
        operation_id = self.alias_container.get_operation_id(presenter, handler)

        # make the callback return the raw HTTPResponse object
        operation_id +=  "_without_preload_content"

        endpoint_callback = getattr(generated_api, operation_id, None)
        if endpoint_callback == None:
            raise ApiException(500, f"Endpoint {operation_id} not found.")
        return endpoint_callback

    def get_endpoint_definition(self, presenter: str, handler: str) -> dict:
        operation_id = self.alias_container.get_operation_id(presenter, handler)
        return self.definitions[operation_id]
    
    def endpoint_has_body(self, presenter: str, handler: str) -> bool:
        """Returns whether an endpoint request expects a body.

        Args:
            presenter (str): ReCodEx presenter or alias.
            handler (str): ReCodEx handler or alias.

        Returns:
            bool: Returns whether an endpoint request expects a body.
        """
        definition = self.get_endpoint_definition(presenter, handler)
        return "requestBody" in definition
    
    def get_endpoint_params(self, presenter: str, handler: str, method: str) -> list[dict]:
        """Returns a list of endpoint parameters matching the selected method.

        Args:
            presenter (str): ReCodEx presenter or alias.
            handler (str): ReCodEx handler or alias.
            method (str): Either 'path' or 'query'.

        Returns:
            list[dict]: Returns a list of endpoint parameters matching the selected method.
        """
        definition = self.get_endpoint_definition(presenter, handler)

        if "parameters" not in definition:
            return []
        
        # filter params by method
        param_defs_filtered = []
        param_defs = definition["parameters"]
        for param_def in param_defs:
            if method.lower() == param_def["in"]:
                param_defs_filtered.append(param_def)

        return param_defs_filtered
    
    def get_path_params(self, presenter: str, handler: str) -> list[dict]:
        """Returns a list of endpoint path parameters.

        Args:
            presenter (str): ReCodEx presenter or alias.
            handler (str): ReCodEx handler or alias.

        Returns:
            list[dict]: Returns a list of endpoint path parameters.
        """
        return self.get_endpoint_params(presenter, handler, 'path')
    
    def get_query_params(self, presenter: str, handler: str) -> list[dict]:
        """Returns a list of endpoint query parameters.

        Args:
            presenter (str): ReCodEx presenter or alias.
            handler (str): ReCodEx handler or alias.

        Returns:
            list[dict]: Returns a list of endpoint query parameters.
        """
        return self.get_endpoint_params(presenter, handler, 'query')

    def get_query_param(self, presenter: str, handler: str, param_name: str) -> dict|None:
        """Returns a specific endpoint query parameter or None if not found.

        Args:
            presenter (str): ReCodEx presenter or alias.
            handler (str): ReCodEx handler or alias.
            param_name (str): Name of a query parameter.

        Returns:
            Returns a specific endpoint query parameter or None if not found.
        """
        query_params = self.get_query_params(presenter, handler)
        for query_param in query_params:
            if query_param["name"] == param_name or query_param["python_name"] == param_name:
                return query_param
        return None

    def get_presenters(self) -> list[str]:
        """Returns a list of presenters in snake case without the '_presenter' suffix.

        Returns:
            list[str]: Returns a list of presenters in snake case without the '_presenter' suffix.
        """
        return self.alias_container.get_presenters()
    
    def get_handlers(self, presenter) -> list[str]:
        """Returns a list of handlers in snake case without the 'action_' prefix.

        Args:
            presenter (str): The presenter containing the handlers. Can be any presenter alias.

        Returns:
            list[str]: Returns a list of handlers in snake case without the 'action_' prefix.
        """
        return self.alias_container.get_handlers(presenter)
