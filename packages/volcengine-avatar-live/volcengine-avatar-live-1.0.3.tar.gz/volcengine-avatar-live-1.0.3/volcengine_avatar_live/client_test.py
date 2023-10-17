# coding=utf-8

import unittest
import json
import threading
import ctypes

from client import LiveClient
from model import INPUT_MODE_TEXT
from http.server import HTTPServer, BaseHTTPRequestHandler

HTTP_PORT = "6789"
PKG_SIZE = 16000 * 2


class MockHTTPServer(threading.Thread):
    live = None

    class HTTPHandler(BaseHTTPRequestHandler):
        def do_POST(self):
            content_len = int(self.headers.get("Content-Length"))
            content = json.loads(self.rfile.read(content_len))
            if self.path.endswith("/start_live"):
                MockHTTPServer.live = content
            else:
                if (
                    MockHTTPServer.live is None
                    or MockHTTPServer.live["live"]["live_id"] != content["live"]["live_id"]
                    or MockHTTPServer.live["auth"]["appid"] != content["auth"]["appid"]
                ):
                    self.send_error(4000, "error")
                if self.path.endswith("/close_live"):
                    MockHTTPServer.live = None
                if self.path.endswith("/change_play_task"):
                    find = False
                    for p in MockHTTPServer.live["script"]["product_list"]:
                        if p["product_id"] == content["data"]["product_id"]:
                            for s in p["scene_list"]:
                                if s["scene_id"] == content["data"]["scene_id"]:
                                    find = True
                                    break
                            if find:
                                break
                    if not find:
                        self.send_error(4000, "error")
                        return
            self.send_success()

        def send_success(self):
            resp = {
                "code": 1000,
                "message": "success",
            }
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(resp).encode())

        def send_error(self, code: int, message: str):
            resp = {
                "code": code,
                "message": message,
            }
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(resp).encode())

    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        self.server = HTTPServer(("", int(HTTP_PORT)), MockHTTPServer.HTTPHandler)
        self.server.serve_forever()

    def stop(self):
        MockHTTPServer.live = None
        thread_id = 0
        if hasattr(self, "_thread_id"):
            thread_id = self._thread_id
        else:
            for id, thread in threading._active.items():
                if thread is self:
                    thread_id = id
                    break
        res = ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id, ctypes.py_object(SystemExit))
        if res > 1:
            ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id, 0)


class TestLiveClient(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.http_server = MockHTTPServer()
        self.http_server.start()

    @classmethod
    def tearDownClass(self):
        self.http_server.stop()

    def test_http(self):
        cli = (
            LiveClient("localhost:" + HTTP_PORT)
            .build_live("live-id")
            .build_auth("app-id", "token")
            .build_avatar("role", "", "", 2000, None, None, {"voice_type": "male"}, None)
            .build_streaming("rtmp-addr")
            .build_simple_script([(INPUT_MODE_TEXT, "hello"), (INPUT_MODE_TEXT, "world")])
        )
        # test start live
        status, code, message = cli.start_live()
        self.assertEqual(status, 200)
        self.assertEqual(code, 1000)
        self.assertEqual(message, "success")
        self.assertIsNotNone(MockHTTPServer.live)
        # test change play task
        status, code, message = cli.change_play_task(1)
        self.assertEqual(status, 200)
        self.assertEqual(code, 1000)
        self.assertEqual(message, "success")
        # test close live
        status, code, message = cli.close_live()
        self.assertEqual(status, 200)
        self.assertEqual(code, 1000)
        self.assertEqual(message, "success")
        self.assertIsNone(MockHTTPServer.live)


if __name__ == "__main__":
    unittest.main()
