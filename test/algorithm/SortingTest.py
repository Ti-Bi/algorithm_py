import random
from unittest import TestCase

from algorithm import Sorting


__author__ = 'Anatol Bludau'


class TestSorting(TestCase):

    def setUp(self):
        self.sorted_seq = range(100)
        self.sorted_seq_with_doubles = range(100) + range(35, 75)
        self.empty_list = []

        # creation of shuffled lists
        self.seq = list(self.sorted_seq)
        self.seq_with_doubles = list(self.sorted_seq_with_doubles)
        random.shuffle(self.seq)
        random.shuffle(self.seq_with_doubles)

    def test_selection_sort(self):
        Sorting.selection_sort(self.seq)
        self.assertListEqual(self.sorted_seq, self.seq)

    def test_selection_sort_with_empty_list(self):
        Sorting.selection_sort(self.empty_list)
        self.assertListEqual([], self.empty_list)

    def test_insertion_sort(self):
        Sorting.insertion_sort(self.seq)
        self.assertListEqual(self.sorted_seq, self.seq)

    def test_insertion_sort_with_empty_list(self):
        Sorting.selection_sort(self.empty_list)
        self.assertListEqual([], self.empty_list)

    def test_merge_sort(self):
        sorted_list = Sorting.merge_sort(self.seq)
        self.assertListEqual(self.sorted_seq, sorted_list)

    def test_merge_sort_with_doubles(self):
        sorted_list = Sorting.merge_sort(self.seq_with_doubles)
        self.assertListEqual(self.sorted_seq_with_doubles, sorted_list)

    def test_merge_sort_with_doubles(self):
        sorted_list = Sorting.merge_sort([])
        self.assertListEqual([], sorted_list)

    def test_partition(self):
        r_seq = range(55) + range(56, 100)
        random.shuffle(r_seq)
        r_seq = [55] + r_seq
        self.assertEquals(55, Sorting.partition(r_seq, 0, len(r_seq)-1))

    def test_partition_with_one_element(self):
        lst_for_partition = [3]
        Sorting.partition(lst_for_partition, 0, 0)
        self.assertListEqual([3], lst_for_partition)

    def test_partition_consistence(self):
        Sorting.partition(self.seq, 0, len(self.seq)-1)
        self.assertListEqual(self.sorted_seq, sorted(self.seq))

    def test_quick_sort(self):
        Sorting.quick_sort(self.seq)
        self.assertListEqual(self.sorted_seq, self.seq)
