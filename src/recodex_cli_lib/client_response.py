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

    def is_data_valid_json(self):
        try:
            json.loads(self.data)
            return True
        except:
            return False
