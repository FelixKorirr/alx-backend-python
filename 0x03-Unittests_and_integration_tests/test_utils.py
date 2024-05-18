#!/usr/bin/env python3
'''Module 0'''
import unittest
from parameterized import parameterized
import utils
from unittest.mock import patch


class TestAccessNestedMap(unittest.TestCase):
    '''Represents TestAccessNestedMap subclass'''
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        '''This tests the access_nested_map function for its result'''
        result = utils.access_nested_map(nested_map, path)
        self.assertEqual(result, expected_result)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        '''Tests if KeyError is raised for given inputs'''
        with self.assertRaises(KeyError):
            utils.access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    '''Represents TestGetJson subclass'''
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch('utils.get_json')
    def test_get_json(self, url, payload, mock_func):
        '''Mocks HTTP calls'''
        my_url = url
        response = payload

        mock_func.return_value = response

        result = utils.get_json(my_url)

        self.assertEqual(result, response)
        mock_func.assert_called_once_with(my_url)
