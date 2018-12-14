import datetime
import json
import sys
import time
from socket import *
import unittest
from client import presence
import re


class TestClient(unittest.TestCase):
    data = presence()

    def test_response(self):
        self.assertEqual(self.data['response'], 200)

    def test_alert(self):
        self.assertEqual(self.data['alert'], 'message for client')

    def test_time(self):
        time_t = self.data['time']
        self.assertTrue(re.fullmatch(r'\d{2}:\d{2}:\d{2}', time_t))


if __name__ == 'main':
    unittest.main()