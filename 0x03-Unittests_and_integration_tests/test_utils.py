#!/usr/bin/env python3
'''Module 0'''
import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    '''Represents this subclass'''
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        '''This tests the access_nested_map function for its result'''
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected_result)
