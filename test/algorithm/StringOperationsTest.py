__author__ = 'Anatol Bludau'

from unittest import TestCase
from algorithm.StringOperations import StringOperations


class StringOperationsTest(TestCase):

    def test_is_palindromic_string_simple_case(self):
        res = StringOperations.is_palindromic_string("abba")
        self.assertTrue(res)

    def test_is_palindromic_string_fails(self):
        res = StringOperations.is_palindromic_string("fsfsdfsggd")
        self.assertFalse(res)

    def test_is_palindromic_string_empty(self):
        res = StringOperations.is_palindromic_string("")
        self.assertFalse(res)

    def test_is_palindromic_string_none(self):
        res = StringOperations.is_palindromic_string(None)
        self.assertFalse(res)
