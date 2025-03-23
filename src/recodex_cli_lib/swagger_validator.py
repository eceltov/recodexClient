import os

import jsonschema.exceptions
from prance import ResolvingParser
import jsonschema
from jsonschema import validate

def camel_case_to_snake_case(camel_case_string):
    return ''.join(['_' + char.lower() if char.isupper() else char for char in camel_case_string])

class SwaggerValidator:
    def __init__(self):
        # the swagger is located in the 'generated' folder
        dirname = os.path.dirname(__file__)
        filename = os.path.join(dirname, 'generated/swagger.yaml')
        parser = ResolvingParser(filename, backend='openapi-spec-validator')
        self.spec = parser.specification

        # construct dict from operationId (snake case and camel case) to endpoint definitions
        # definitions are identical to swagger definitions (body of method field) with the added 'method' key
        self.definitions = {}
        for path, path_body in self.spec["paths"].items():
            for method, method_body in path_body.items():
                method_body["method"] = method
                operation_id = method_body["operationId"]
                snake_case_operation_id = camel_case_to_snake_case(operation_id)
                self.definitions[operation_id] = method_body
                self.definitions[snake_case_operation_id] = method_body

    def get_definition_by_operation_id(self, operation_id):
        return self.definitions[operation_id]

    def validate_params(self, operation_id, method, params):
        definition = self.get_definition_by_operation_id(operation_id)
        param_defs = definition["parameters"]
        for param_def in param_defs:
            # check if correct method
            if method != param_def["in"]:
                continue

            param_name = param_def["name"]
            # check if param is absent
            if param_name not in params:
                # fail validation if it is required
                if param_def["required"]:
                    raise jsonschema.exceptions.ValidationError(f"Param '{param_name}' is required.")
                # skip if it is not required
                continue

            validate(params[param_name], param_def["schema"])

    # converts a generated body instance to a dictionary
    def convert_generated_to_dict(self, generated_body):
        # this dict contains the body parameters with a '_' prefix
        raw_dict = generated_body.__dict__
        refined_dict = {}
        # keep keys with the prefix
        for key, value in raw_dict.items():
            if key[0] == '_':
                # remove the prefix
                refined_dict[key[1:]] = value
        return refined_dict

    def validate_body(self, operation_id, body):
        definition = self.get_definition_by_operation_id(operation_id)
        # skip if there is no body definition
        if "requestBody" not in definition:
            return
      
        schema = definition["requestBody"]["content"]["application/json"]["schema"]
        validate(body, schema)

    def validate(self, operation_id, body={}, path_params={}, query_params={}):
        self.validate_params(operation_id, "path", path_params)
        self.validate_params(operation_id, "query", query_params)

        # convert generated body objects to a dict    
        if type(body) is dict:
            body_dict = body
        else:
            body_dict = self.convert_generated_to_dict(body)
        self.validate_body(operation_id, body_dict)
