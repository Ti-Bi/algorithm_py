__author__ = 'Anatol Bludau'

from unittest import TestCase
from algorithm.StringOperations import StringOperations


class StringOperationsTest(TestCase):

    """
    -------------------------------------------------------------------------------------------
    ### is_palindromic_string()
    -------------------------------------------------------------------------------------------
    """

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

    def test_is_palindromic_string_one_symbol(self):
        res = StringOperations.is_palindromic_string("f")
        self.assertTrue(res)

    """
    -------------------------------------------------------------------------------------------
    ### find_the_largest_palindromic_substring_brut_force()
    -------------------------------------------------------------------------------------------
    """

    def test_find_the_largest_palindromic_substring_brut_force_simple_case(self):
        res = StringOperations.find_the_largest_palindromic_substring_brut_force("testtset")
        self.assertEqual("testtset", res)

    def test_find_the_largest_palindromic_substring_brut_force_empty_string(self):
        res = StringOperations.find_the_largest_palindromic_substring_brut_force("")
        self.assertIsNone(res)

    def test_find_the_largest_palindromic_substring_brut_force_none_string(self):
        res = StringOperations.find_the_largest_palindromic_substring_brut_force(None)
        self.assertIsNone(res)

    def test_find_the_largest_palindromic_substring_brut_force_complicated_case(self):
        res = StringOperations.find_the_largest_palindromic_substring_brut_force("sd;glolsd sk alskdghh ;asdkgstesttsetfjalsdhgakjsgupagdfap9weog")
        self.assertEqual("testtset", res)

    def test_find_the_largest_palindromic_substring_brut_force_string_without_palindromic_substring(self):
        res = StringOperations.find_the_largest_palindromic_substring_brut_force("abcdefghijklmnopqrstuvwxyz")
        self.assertIsNone(res)

    def test_find_the_largest_palindromic_substring_brut_force_one_letter(self):
        res = StringOperations.find_the_largest_palindromic_substring_brut_force("f")
        self.assertEqual("f", res)

    """
    -------------------------------------------------------------------------------------------
    ### find_the_largest_palindromic_substring_matrix()
    -------------------------------------------------------------------------------------------
    """
"""
    def test_find_the_largest_palindromic_substring_matrix_simple_case(self):
        res = StringOperations.find_the_largest_palindromic_substring_matrix("testtset")
        self.assertEqual("testtset", res)

    def test_find_the_largest_palindromic_substring_matrix_empty_string(self):
        res = StringOperations.find_the_largest_palindromic_substring_matrix("")
        self.assertIsNone(res)

    def test_find_the_largest_palindromic_substring_matrix_none_string(self):
        res = StringOperations.find_the_largest_palindromic_substring_matrix(None)
        self.assertIsNone(res)

    def test_find_the_largest_palindromic_substring_matrix_complicated_case(self):
        res = StringOperations.find_the_largest_palindromic_substring_matrix("sd;glolsd sk alskdghh ;asdkgstesttsetfjalsdhgakjsgupagdfap9weog")
        self.assertEqual("testtset", res)

    def test_find_the_largest_palindromic_substring_matrix_string_without_palindromic_substring(self):
        res = StringOperations.find_the_largest_palindromic_substring_matrix("abcdefghijklmnopqrstuvwxyz")
        self.assertIsNone(res)

    def test_find_the_largest_palindromic_substring_matrix_one_letter(self):
        res = StringOperations.find_the_largest_palindromic_substring_matrix("f")
        self.assertEqual("f", res)

    def test_find_the_largest_palindromic_substring_matrix_one_letter(self):
        res = StringOperations.find_the_largest_palindromic_substring_matrix("hhyasag")
        self.assertEqual("asa", res)
        """