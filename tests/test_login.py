# test_my_module.py
import unittest
from unittest.mock import patch, MagicMock
import json

# # Import the module you want to test
# import req

from recodex_cli_lib.client_factory import get_client

client = get_client("http://localhost:4000", "user", "password")

# client.generated_api.api_client.rest_client.pool_manager

class TestMyModule(unittest.TestCase):

    @patch('client.generated_api.api_client.rest_client.pool_manager')
    def test_fetch_data_success(self, mock_pool_manager):
        # Configure the mock to return a successful response
        mock_response = MagicMock()
        mock_response.status = 200
        mock_response.data = json.dumps({"key": "value"}).encode('utf-8')
        mock_pool_manager.return_value = mock_response

        # Call the function being tested
        result = client.send_request("groups", "default")

        # Assertions
        self.assertEqual(result, {"key": "value"})
        mock_pool_manager.assert_called_once_with('GET', "http://example.com/api/data")

    # ... more tests

unittest.main(verbosity=2)

# from recodex_cli_lib.client_factory import get_client
# import unittest
# from unittest import mock
# import json

# import urllib3

# class TestLambdaHandler(unittest.TestCase):

#     @mock.patch('urllib3.PoolManager')
#     def test_lambda_handler(self, mock_PoolManager):
#         from lambda_handler import func
#         mock_http = mock_PoolManager.return_value
#         event = {}
#         func(event, [])
#         mock_http.request.assert_called_once_with('POST', 'http://localhost:3000', body=json.dumps({'attribute': 'value'}).encode('utf-8'))


# unittest.main(verbosity=2)

# def test_mock(requests_mock):
#         requests_mock.get('http://qwerqwerqwerqrqwewereqwrqwr.com', text='resp')

#         # Creating a PoolManager instance for sending requests.
#         http = urllib3.PoolManager()

#         # Sending a GET request and getting back response as HTTPResponse object.
#         resp = http.request("GET", "http://qwerqwerqwerqrqwewereqwrqwr.com")
#         assert resp.data == 'resp'

# def test_login_success(requests_mock):
#     # 1. Arrange: Set up the mock response
#     # The 'm' argument is provided by the @requests_mock.Mocker decorator
#     requests_mock.register_uri('POST', 'http://localhost:4000/v1/login', json={'username': 'user', 'password': 'password'})

#     # 2. Act: Instantiate the wrapper and call the method INSIDE the test function
#     # The ApiClient inside MyApiWrapper will now be created in a mocked environment
#     client = get_client("http://localhost:4000", "user", "password")
#     client.send_request("groups", "default")

#     print("a")

#     assert requests_mock.called
#     assert requests_mock.call_count == 1

# def test_get_user_name_success():

#     # You might need to configure the host in your generated client's configuration
#     wrapper = MyApiWrapper()
#     user_name = wrapper.get_user_name(1)

#     assert user_name == 'John Doe'
#     assert adapter.called
#     assert adapter.call_count == 1

# def test_get_user_name_not_found():
#     adapter = requests_mock.Adapter()
#     adapter.register_uri('GET', 'http://api.example.com/users/2', status_code=404)

#     wrapper = MyApiWrapper()
#     user_name = wrapper.get_user_name(2)

#     assert user_name is None