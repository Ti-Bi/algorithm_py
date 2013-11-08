import random
from unittest import TestCase
from bludau.study.algorithm.sorting.Sorting import Sorting

__author__ = 'Anatol Bludau'


class TestSorting(TestCase):

    def setUp(self):
        self.sorted_seq = range(100)
        self.seq = range(100)
        random.shuffle(self.seq)

    def test_selection_sort(self):
        Sorting.selection_sort(self.seq)
        self.assertListEqual(self.sorted_seq, self.seq, 'The list is not equals')

    def test_selection_sort_with_empty_list(self):
        empty_list = []
        Sorting.selection_sort(empty_list)
        self.assertListEqual([], empty_list, 'The list is not empty')