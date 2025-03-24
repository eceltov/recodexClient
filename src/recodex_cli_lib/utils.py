def camel_case_to_snake_case(camel_case_string):
    return ''.join(['_' + char.lower() if char.isupper() else char for char in camel_case_string])
