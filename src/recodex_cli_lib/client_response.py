import json

from .generated.swagger_client.rest import RESTResponse

class ClientResponse():
    def __init__(self, response: RESTResponse):
        self.urllib3_response = response.urllib3_response
        self.status = response.status
        self.reason = response.reason
        self.data_binary = response.data
        self.headers = response.getheaders()
        self.data = response.data.decode("utf-8")

    def get_json_data(self) -> dict|bool:
        """Parses response payload as a JSON string.

        Returns:
            dict|bool: A dictionary constructed from the payload, or False if the data is not in JSON format.
        """
        try:
            return json.loads(self.data)
        except:
            return False

        