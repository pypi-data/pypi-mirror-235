# coding=utf-8

import unittest
import util


class TestUtil(unittest.TestCase):
    def test_generate_log_id(self):
        log_id = util.generate_log_id()
        self.assertEqual(len(log_id), 34)


if __name__ == "__main__":
    unittest.main()
