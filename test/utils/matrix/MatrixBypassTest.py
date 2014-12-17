__author__ = 'anatolbludau'

from unittest import TestCase
from utils.matrix.MatrixBypass import MatrixBypass


class MatrixBypassTest(TestCase):

    def test_simple(self):
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        MatrixBypass.simple(matrix)

    def test_simple_none(self):
        MatrixBypass.simple(None)

    def test_simple_empty(self):
        MatrixBypass.simple([])

    def test_sample_empty_row(self):
        MatrixBypass.simple([[]])