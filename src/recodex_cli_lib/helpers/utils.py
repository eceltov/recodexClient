from collections.abc import Callable

def camel_case_to_snake_case(camel_case_string):
    return ''.join(['_' + char.lower() if char.isupper() else char for char in camel_case_string])

def parse_endpoint_function(endpoint: Callable) -> tuple[str, str]:
    """Extracts the presenter and handler names from a generated endpoint function.

    Args:
        endpoint (Callable): A generated endpoint function.

    Returns:
        tuple[str]: Returns a (presenter, handler) tuple.
    """

    name = endpoint.__name__
    presenter_pos = name.find("_presenter")
    action_pos = name.find("action_")
    presenter = name[:presenter_pos]
    handler = name[action_pos:]

    return (presenter, handler)

def preprocess_raw_input_data(
        path_params: dict,
        query_params: dict,
        presenter: str,
        handler: str,
        endpoint_resolver
    ) -> tuple[dict, dict]:

    processed_path_params = __parse_input_values(path_params, presenter, handler, endpoint_resolver.get_path_param)
    processed_query_params = __parse_input_values(query_params, presenter, handler, endpoint_resolver.get_query_param)
    return (processed_path_params, processed_query_params)

def __parse_input_values(params: dict, presenter: str, handler: str, param_definition_callback: Callable) -> dict:
    processed_params = {}
    for key, value in params.items():
        param_definition = param_definition_callback(presenter, handler, key)
        processed_params[key] = value

        # skip undefined parameters or parameters that are not stringified
        if param_definition == None or (not isinstance(value, str)):
            continue

        type = param_definition['schema']['type']
        if type == "boolean":
            if value.lower() == 'true':
                processed_params[key] = True
            elif value.lower() == 'false':
                processed_params[key] = False
            # keep invalid values for jsonschema errors
        elif type == "number" or type == "integer":
            try:
                if type == "integer":
                    processed_params[key] = int(value)
                else:
                    processed_params[key] = float(value)
            except:
                # keep invalid values for jsonschema errors
                pass
    return processed_params