#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_list_is_empty(self):
        self.assertIsNone(max_integer([]))

    def test_is_integer(self):
        self.assertEqual(max_integer([1, 2, 3]), 3)

    def test_is_negative(self):
        self.assertEqual(max_integer([-2, -3, -4]), -2)

    def test_mixed_numbers(self):
        self.assertEqual(max_integer([-3, 26, -4, 7]), 26)

    def test_string_input(self):
        self.assertEqual(max_integer("Hello world"), "w")

    def test_list_of_string(self):
        self.assertEqual(max_integer(["hello", "world"]), "world")

    def test_is_set(self):
        self.assertEqual(max_integer(("a", "b", "c")), "c")

    def test_is_float(self):
        self.assertEqual(max_integer([2.4, 3.6, 1.7]), 3.6)

    def test_list_of_one_element(self):
        self.assertEqual(max_integer([52]), 52)
