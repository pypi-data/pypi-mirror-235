# coding=utf-8

import unittest

from model import Live, Auth, Avatar, Streaming, Content, Scene, Product, Script, INPUT_MODE_TEXT, INPUT_MODE_AUDIO


class TestModel(unittest.TestCase):
    def test_live(self):
        with self.assertRaises(ValueError):
            live = Live("")
        live = Live("live_id")
        self.assertIsNotNone(live)

    def test_auth(self):
        with self.assertRaises(ValueError):
            auth = Auth("", "token")
        with self.assertRaises(ValueError):
            auth = Auth("appid", "")
        auth = Auth("appid", "token")
        self.assertIsNotNone(auth)

    def test_avatar(self):
        with self.assertRaises(ValueError):
            avatar = Avatar("", "dh_type", "", 0, {}, {}, {"voice_type": "male"}, {})
        with self.assertRaises(ValueError):
            avatar = Avatar("role", "dh_type", "", 99, {}, {}, {"voice_type": "male"}, {})
        with self.assertRaises(ValueError):
            avatar = Avatar("role", "dh_type", "", 100, {}, {}, {}, {})
        avatar = Avatar("role", "dh_type", "", 2000, {}, {}, {"voice_type": "male"}, {})
        self.assertIsNotNone(avatar)

    def test_streaming(self):
        with self.assertRaises(ValueError):
            streaming = Streaming("")
        streaming = Streaming("rtmp_addr")
        self.assertIsNotNone(streaming)

    def test_content(self):
        with self.assertRaises(ValueError):
            content = Content("invalid", "hello")
        with self.assertRaises(ValueError):
            content = Content(INPUT_MODE_TEXT, "")
        with self.assertRaises(ValueError):
            content = Content(INPUT_MODE_AUDIO, "")
        content = Content(INPUT_MODE_TEXT, "hello")
        self.assertIsNotNone(content)

    def test_scene(self):
        with self.assertRaises(ValueError):
            scene = Scene([])
        content = Content(INPUT_MODE_TEXT, "hello")
        scene = Scene([content])
        self.assertIsNotNone(scene)

    def test_product(self):
        with self.assertRaises(ValueError):
            product = Product([])
        content = Content(INPUT_MODE_TEXT, "hello")
        scene = Scene([content])
        product = Product([scene])
        self.assertIsNotNone(product)

    def test_script(self):
        with self.assertRaises(ValueError):
            script = Script([])
        content = Content(INPUT_MODE_TEXT, "hello")
        scene = Scene([content])
        product = Product([scene])
        script = Script([product])
        self.assertIsNotNone(script)


if __name__ == "__main__":
    unittest.main()
