import datetime
import json
import sys
import time
from socket import *
import unittest
from server import presence_response
import re


class TestServerResponse(unittest.TestCase):
    response_test = presence_response()

    def test_response(self):
        self.assertEqual(self.response_test['response'], 200)

    def test_equal(self):
        self.assertEqual(self.response_test['alert'], 'message for client')

    def test_time(self):
        time_t = self.response_test['time']
        self.assertTrue(re.fullmatch(r'\d{2}:\d{2}:\d{2}', time_t))




if __name__ == 'main':
    unittest.main()