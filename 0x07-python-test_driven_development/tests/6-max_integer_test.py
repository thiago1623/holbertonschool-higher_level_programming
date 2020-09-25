#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """program that make check if to the entire original program"""

    def test_max_intlist(self):
        """ Test list with intergers"""
        new_list = [10, 15, 58]
        self.assertEqual(max_integer(new_list), 58)

    def test_max_floatlist(self):
        """ Test when a list of floats is passed """
        new_list = [1.5, 4]
        self.assertEqual(max_integer(new_list), 4)

    def test_max_floatlist_neg(self):
        """ Test when a list of neg floats is passed """
        new_list = [-2.08, -3.2, -7.5, -10.0]
        self.assertEqual(max_integer(new_list), -2.08)

    def test_max_empty(self):
        """ Test when an empty list function is passed """
        new_list = []
        self.assertEqual(max_integer(new_list), None)

    def test_max_repeatedint(self):
        """ Test when a single int is passed as list """
        new_list = [4, 4, 4]
        self.assertEqual(max_integer(new_list), 4)

    def test_max_nolistint(self):
        """ Test when an integer is passed to function """
        with self.assertRaises(TypeError):
            max_integer(10)

    def test_max_char(self):
        """ Test when a list of chars is passed """
        new_list = ["1", "2", "a", "4"]
        self.assertEqual(max_integer(new_list), 'a')

    def test_max_liststromt(self):
        """ Test when a list with number and string is passed """
        new_list = [1, "Hola"]
        with self.assertRaises(TypeError):
            max_integer(new_list)

    def test_max_intlist_neg(self):
        """ Test list with intergers"""
        self.assertEqual(max_integer([-5, -15]), -5)
