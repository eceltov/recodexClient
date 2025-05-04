import os

import jsonschema.exceptions
from prance import ResolvingParser
import jsonschema
from jsonschema import validate

class SwaggerValidator:
    def validate_params(self, endpoint_definition, method, params):
        # skip validation if the endpoint does not expect any
        if "parameters" not in endpoint_definition:
            return
        
        param_defs = endpoint_definition["parameters"]
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

    def validate_body(self, endpoint_definition: dict, body):
        # skip if there is no body definition
        if "requestBody" not in endpoint_definition:
            return
      
        schema = endpoint_definition["requestBody"]["content"]["application/json"]["schema"]
        validate(body, schema)

    def validate(self, endpoint_definition: dict, body={}, path_params={}, query_params={}):
        self.validate_params(endpoint_definition, "path", path_params)
        self.validate_params(endpoint_definition, "query", query_params)

        # convert generated body objects to a dict    
        if type(body) is dict:
            body_dict = body
        else:
            body_dict = self.convert_generated_to_dict(body)
        self.validate_body(endpoint_definition, body_dict)
