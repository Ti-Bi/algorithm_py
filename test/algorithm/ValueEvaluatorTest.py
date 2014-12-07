__author__ = 'Anatol Bludau'

from unittest import TestCase
from algorithm.ValueEvaluator import ValueEvaluator


class ValueEvaluatorTest(TestCase):
    """
    The set of testes for testing value evaluators.
    """

    def test_eval_reverse_polish_notation_empty_string(self):
        res = ValueEvaluator.eval_reverse_polish_notation("")
        self.assertIsNone(res)

    def test_eval_reverse_polish_notation_string_none(self):
        res = ValueEvaluator.eval_reverse_polish_notation(None)
        self.assertIsNone(res)

    def test_eval_reverse_polish_notation_string_simple_sum(self):
        val = "2 3 +"
        res = ValueEvaluator.eval_reverse_polish_notation(val)
        self.assertEqual(5, res)

    def test_eval_reverse_polish_notation_string_simple_sub(self):
        val = "2 3 -"
        res = ValueEvaluator.eval_reverse_polish_notation(val)
        self.assertEqual(-1, res)

    def test_eval_reverse_polish_notation_string_simple_multiply(self):
        val = "2 3 *"
        res = ValueEvaluator.eval_reverse_polish_notation(val)
        self.assertEqual(6, res)

    def test_eval_reverse_polish_notation_string_simple_sum(self):
        val = "2 3 /"
        res = ValueEvaluator.eval_reverse_polish_notation(val)
        self.assertEqual(float(2) / 3, res)

    def test_eval_reverse_polish_notation_list_empty_list(self):
        res = ValueEvaluator.eval_reverse_polish_notation_list([])
        self.assertIsNone(res)

    def test_eval_reverse_polish_notation_list_none(self):
        res = ValueEvaluator.eval_reverse_polish_notation_list(None)
        self.assertIsNone(res)

    def test_eval_reverse_polish_notation_list_simple_case_plus(self):
        val = [1, 2, "+"]
        res = ValueEvaluator.eval_reverse_polish_notation_list(val)
        self.assertEqual(3, res)

    def test_eval_reverse_polish_notation_list_simple_case_sub(self):
        val = [1, 2, "-"]
        res = ValueEvaluator.eval_reverse_polish_notation_list(val)
        self.assertEqual(-1, res)

    def test_eval_reverse_polish_notation_list_simple_case_multiplication(self):
        val = [1, 2, "*"]
        res = ValueEvaluator.eval_reverse_polish_notation_list(val)
        self.assertEqual(2, res)

    def test_eval_reverse_polish_notation_list_simple_case_division(self):
        val = [1, 2, "/"]
        res = ValueEvaluator.eval_reverse_polish_notation_list(val)
        self.assertAlmostEqual(0.5, res)

    def test_eval_reverse_polish_notation_list_complex_formula(self):
        val = [1, 2, "+", 4, "*", 6, "/", 4, '-']
        res = ValueEvaluator.eval_reverse_polish_notation_list(val)
        self.assertAlmostEqual(-2, res)

