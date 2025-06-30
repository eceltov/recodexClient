import unittest
from multiprocessing import Process
import time
import time

from recodex_cli_lib.client_factory import get_client
from .mock_server import create_app

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

    def test_fetch_data_from_flask_server(self):
        res = self.client.send_request("groups", "default").get_parsed_data()
        self.assertNotEqual(res, False)
        self.assertEqual(res["payload"][0]["id"], "10000000-2000-4000-8000-160000000000")

unittest.main(verbosity=2)
