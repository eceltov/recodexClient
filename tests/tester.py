import unittest
from multiprocessing import Process
import time
from flask import Flask, request, jsonify
import jwt
import time

from recodex_cli_lib.client_factory import get_client

app = Flask(__name__)
import logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

@app.route('/v1/login', methods=['POST'])
def get_data():
    received_data = request.get_json()
    token = jwt.encode(
        {
            "test": "value",
            "iat": time.time(),
            "exp": time.time() + 10000,
            "username": received_data["username"],
            "password": received_data["password"],
        },
        "key",
    )
    print(token)
    return jsonify({"payload": {"accessToken": token}}), 200


@app.route('/v1/groups', methods=['GET'])
def get_group():
    return jsonify(
        {
            "success": True,
            "code": 200,    
            "payload": [    
                {
                "id": "10000000-2000-4000-8000-160000000000",
                }
            ]
        }
    ), 200

class TestMyModuleWithFlaskServer(unittest.TestCase):
    PORT = 8081
    SERVER_URL = f"http://localhost:{PORT}"
    flask_app = app # use the global server handle

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
