import unittest
from multiprocessing import Process
import time

from recodex_cli_lib.client_factory import get_client
from recodex_cli_lib.helpers.file_upload_helper import upload
from recodex_cli_lib.generated.swagger_client.api.default_api import DefaultApi

from .mock_server import create_app
from .utils import constants

class TestMyModuleWithFlaskServer(unittest.TestCase):
    PORT = 8081
    SERVER_URL = f"http://localhost:{PORT}"
    flask_app = create_app() # use the global server handle

    @classmethod
    def setUpClass(cls):
        # start the mock server in a separate thread
        cls.flask_server_thread = Process(
            target=lambda: cls.flask_app.run(port=cls.PORT, debug=False, use_reloader=False)
        )
        cls.flask_server_thread.daemon = True
        cls.flask_server_thread.start()
        # wait for the server to start
        time.sleep(0.5)
        # initialize client
        cls.client = get_client(cls.SERVER_URL, "user", "password")

    @classmethod
    def tearDownClass(cls):
        cls.flask_server_thread.terminate()
        cls.flask_server_thread.join(timeout=2)

    # test the send_request method on the groups.default endpoint
    def test_get_groups_info(self):
        res = self.client.send_request("groups", "default").get_parsed_data()
        self.assertNotEqual(res, False)
        self.assertEqual(res["payload"][0]["id"], constants.uuid)

    # test the send_request_by_callback method on the groups.default endpoint
    def test_get_groups_info_callback(self):
        res = self.client.send_request_by_callback(DefaultApi.groups_presenter_action_default).get_parsed_data()
        self.assertNotEqual(res, False)
        self.assertEqual(res["payload"][0]["id"], constants.uuid)

    # test the file upload utility function
    def test_upload_file(self):
        id = upload(self.client, "tests/utils/uploadTestFile.txt")
        self.assertEqual(id, constants.uuid)

unittest.main(verbosity=2)
