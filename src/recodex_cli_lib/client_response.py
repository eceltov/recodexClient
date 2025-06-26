import json
import yaml

from urllib3.response import HTTPResponse

class ClientResponse():
    def __init__(self, response: HTTPResponse):
        self.status = response.status
        self.reason = response.reason
        self.data_binary = response.data
        self.headers = response.getheaders()
        self.data = response.data.decode("utf-8")

    def __get_parsed_data_or_throw(self) -> dict:
        return json.loads(self.data)
    
    def get_parsed_data(self) -> dict | bool:
        """Parses response payload as a JSON string.

        Returns:
            dict|bool: A dictionary constructed from the payload, or False if the data is not in JSON format.
        """
        try:
            return self.__get_parsed_data_or_throw()
        except:
            return False
        

    def get_json_string(self, minimized: bool = False) -> str:
        if minimized:
            return self.data
        try:
            return json.dumps(self.__get_parsed_data_or_throw(), indent=2, ensure_ascii=False)
        except:
            raise Exception("The response data is not in JSON format.")
    
    def get_yaml_string(self, minimized: bool = False) -> str:
        try:
            if minimized:
                return yaml.dump(self.__get_parsed_data_or_throw(), default_flow_style=True, indent=None, allow_unicode=True)
            return yaml.dump(self.__get_parsed_data_or_throw(), allow_unicode=True, indent=2)
        except:
            raise Exception("The response data could not be converted to YAML.")
