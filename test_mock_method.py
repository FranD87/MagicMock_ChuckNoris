import unittest
import json
from unittest.mock import patch, MagicMock
from MagicMock_ChuckNoris.method import get_chuck_norris_joke


class Get_Chuck_Norris_JokeTest(unittest.TestCase):

    @patch('method.requests')
    def test_joke(self, requests_mock):
        with open('chuck_norris_response.json', 'r') as file:
            body = json.load(file)
        requests_response_mock = MagicMock()
        requests_response_mock.status_code = 200
        requests_response_mock.json.return_value = body
        requests_mock.get.return_value = requests_response_mock
        self.assertEqual("Chuck Norris smashed microsofsts window", get_chuck_norris_joke())

    @patch('method.requests')
    def test_success(self, request_mock):
        request_response_mock = MagicMock()
        request_response_mock.status_code = 200
        request_response_mock.json.return_value = {'value':  "Chuck Norris smashed microsofsts window"}
        request_mock.get.return_value = request_response_mock
        self.assertEqual("Chuck Norris smashed microsofsts window", get_chuck_norris_joke())

    @patch('method.requests')
    def test_NotSuccessful(self, request_mock):
        request_response_mock = MagicMock()
        request_response_mock.status_code = 404
        request_mock.get.return_value = request_response_mock
        with self.assertRaises(RuntimeError):
            get_chuck_norris_joke()




