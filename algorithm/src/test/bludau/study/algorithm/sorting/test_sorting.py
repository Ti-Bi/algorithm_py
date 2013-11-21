import random
from unittest import TestCase
from bludau.study.algorithm.sorting.Sorting import Sorting

__author__ = 'Anatol Bludau'


class TestSorting(TestCase):

    def setUp(self):
        self.sorted_seq = range(100)
        self.sorted_seq_with_doubles = range(100) + range(35, 75)

        # creation of shuffled lists
        self.seq = list(self.sorted_seq)
        self.seq_with_doubles = list(self.sorted_seq_with_doubles)
        random.shuffle(self.seq)
        random.shuffle(self.seq_with_doubles)

    def test_selection_sort(self):
        Sorting.selection_sort(self.seq)
        self.assertListEqual(self.sorted_seq, self.seq)

    def test_selection_sort_with_empty_list(self):
        empty_list = []
        Sorting.selection_sort(empty_list)
        self.assertListEqual([], empty_list)

    def test_insertion_sort(self):
        Sorting.insertion_sort(self.seq)
        self.assertListEqual(self.sorted_seq, self.seq)

    def test_insertion_sort_with_empty_list(self):
        empty_list = []
        Sorting.selection_sort(empty_list)
        self.assertListEqual([], empty_list)

    def test_merge_sort(self):
        sorted = Sorting.merge_sort(self.seq)
        self.assertListEqual(self.sorted_seq, sorted)

    def test_merge_sort_with_doubles(self):
        sorted = Sorting.merge_sort(self.seq_with_doubles)
        self.assertListEqual(self.sorted_seq_with_doubles, sorted)

    def test_merge_sort_with_doubles(self):
        sorted = Sorting.merge_sort([])
        self.assertListEqual([], sorted)