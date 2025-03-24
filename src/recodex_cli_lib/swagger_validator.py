import os

import jsonschema.exceptions
from prance import ResolvingParser
import jsonschema
from jsonschema import validate
from .utils import camel_case_to_snake_case
from .endpoint_resolver import EndpointResolver

class SwaggerValidator:
    def __init__(self, endpoint_resolver):
        self.endpoint_resolver: EndpointResolver = endpoint_resolver

    def validate_params(self, presenter, endpoint, method, params):
        definition = self.endpoint_resolver.get_endpoint_definition(presenter, endpoint)
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

    def validate_body(self, presenter, endpoint, body):
        definition = self.endpoint_resolver.get_endpoint_definition(presenter, endpoint)
        # skip if there is no body definition
        if "requestBody" not in definition:
            return
      
        schema = definition["requestBody"]["content"]["application/json"]["schema"]
        validate(body, schema)

    def validate(self, presenter, endpoint, body={}, path_params={}, query_params={}):
        self.validate_params(presenter, endpoint, "path", path_params)
        self.validate_params(presenter, endpoint, "query", query_params)

        # convert generated body objects to a dict    
        if type(body) is dict:
            body_dict = body
        else:
            body_dict = self.convert_generated_to_dict(body)
        self.validate_body(presenter, endpoint, body_dict)
