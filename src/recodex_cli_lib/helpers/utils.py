from collections.abc import Callable

def camel_case_to_snake_case(camel_case_string):
    return ''.join(['_' + char.lower() if char.isupper() else char for char in camel_case_string])

def parse_endpoint_function(endpoint: Callable) -> tuple[str]:
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
