import os
import yaml
from .utils import camel_case_to_snake_case
import jsonschema.exceptions
from prance import ResolvingParser
import jsonschema
from jsonschema import validate

class AliasContainer:
    def __init__(self, definitions):
        self.definitions = definitions
        self.__presenter_suffix = '_presenter'

        self.__init_raw_resolve_dict()
        self.__init_default_aliases()

    def __init_raw_resolve_dict(self):
        # create a map from raw (with the 'presenter'/'action' prefix/suffix) presenter names to endpoints
        raw_presenter_to_endpoint_map: dict[str, list[str]] = {}
        for operation_id in self.definitions.keys():
            presenter_pos = operation_id.find(self.__presenter_suffix)
            if presenter_pos == -1:
                raise RuntimeError(f"The operationId '{operation_id}' does not contain the '{self.__presenter_suffix}' substring")

            presenter_name = operation_id[0 : presenter_pos] + self.__presenter_suffix
            endpoint_name = operation_id[presenter_pos + len(self.__presenter_suffix) + 1 :]

            if presenter_name in raw_presenter_to_endpoint_map:
                raw_presenter_to_endpoint_map[presenter_name].append(endpoint_name)
            else:
                raw_presenter_to_endpoint_map[presenter_name] = [ endpoint_name ]
        self.raw_presenter_to_endpoint_map = raw_presenter_to_endpoint_map

    def __init_default_aliases(self):
        # maps aliases to raw presenter name
        presenter_aliases: dict[str, str] = {}
        for presenter_name in self.raw_presenter_to_endpoint_map.keys():
            # keep the raw name as a valid alias
            presenter_aliases[presenter_name] = presenter_name

            # add raw name without the '_presenter' suffix
            shortened_name = presenter_name[: -len(self.__presenter_suffix)]
            presenter_aliases[shortened_name] = presenter_name
        self.presenter_aliases = presenter_aliases

        # maps raw presenter names to a dict from endpoint aliases to raw endpoint names
        endpoint_aliases: dict[str, dict[str, str]] = {}
        for presenter_name, endpoint_names in self.raw_presenter_to_endpoint_map.items():
            aliases = {}
            for endpoint_name in endpoint_names:
                # keep the raw name as a valid alias
                aliases[endpoint_name] = endpoint_name

                # add raw name without the 'action_' prefix
                shortened_name = endpoint_name[len('action_') :]
                aliases[shortened_name] = endpoint_name
            endpoint_aliases[presenter_name] = aliases
        self.endpoint_aliases = endpoint_aliases

    def __get_raw_presenter_name_or_throw(self, presenter):
        if presenter not in self.presenter_aliases:
            raise RuntimeError(f"'{presenter}' is not a known presenter name or alias.")
        return self.presenter_aliases[presenter]

    def __get_raw_endpoint_name_or_throw(self, presenter, endpoint):
        raw_presenter_name = self.__get_raw_presenter_name_or_throw(presenter)
        aliases = self.endpoint_aliases[raw_presenter_name]
        if endpoint not in aliases:
            raise RuntimeError(f"'{endpoint}' is not a known endpoint name or alias.")
        return aliases[endpoint]

    def add_presenter_alias(self, presenter, alias):
        raw_presenter_name = self.__get_raw_presenter_name_or_throw(presenter)
        
        if alias in self.presenter_aliases:
            raise RuntimeError(f"The presenter alias '{alias}' is already registered"
                + f"for the '{self.presenter_aliases[alias]}' presenter")
        
        # the value has to be the raw presenter name
        self.presenter_aliases[alias] = raw_presenter_name


    def add_endpoint_alias(self, presenter, endpoint, alias):
        raw_presenter_name = self.__get_raw_presenter_name_or_throw(presenter)
        raw_endpoint_name = self.__get_raw_endpoint_name_or_throw(presenter, endpoint)
        aliases = self.endpoint_aliases[raw_presenter_name]

        if alias in aliases:
            raise RuntimeError(f"The endpoint alias '{alias}' is already registered"
                + f"for the '{aliases[alias]}' endpoint")
        
        # the value has to be the raw endpoint name
        aliases[alias] = raw_endpoint_name

    def get_operation_id(self, presenter, endpoint):
        raw_presenter_name = self.__get_raw_presenter_name_or_throw(presenter)
        raw_endpoint_name = self.__get_raw_endpoint_name_or_throw(presenter, endpoint)
        return f"{raw_presenter_name}_{raw_endpoint_name}"

class EndpointResolver:
    def __init__(self, generated_client):
        self.generated_client = generated_client

        # load aliases.yaml
        self.__load_aliases()

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


    def __load_aliases(self):
        dirname = os.path.dirname(__file__)
        filepath = os.path.join(dirname, 'aliases.yaml')
        with open(filepath) as file:
            self.aliases: dict[str, dict] = yaml.safe_load(file)

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

        for presenter, presenter_alias_obj in self.aliases.items():
            if 'alias' in presenter_alias_obj:
                self.alias_container.add_presenter_alias(presenter, presenter_alias_obj['alias'])

            if 'endpoints' not in presenter_alias_obj:
                continue

            for endpoint, endpoint_alias in presenter_alias_obj['endpoints'].items():
                self.alias_container.add_endpoint_alias(presenter, endpoint, endpoint_alias)


    # endpointId should be in 'presenter.endpoint' format, such as 'test_presenter.action_debug'
    def __resolve(endpoint_id):
        pass

    def get_definition_by_operation_id(self, operation_id):
        return self.definitions[operation_id]
