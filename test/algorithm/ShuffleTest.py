from unittest import TestCase

from algorithm import Shuffle


__author__ = 'Anatol Bludau'


class TestShuffle(TestCase):

    def setUp(self):
        self.seq = range(10)

    def test_linear_shuffle(self):
        Shuffle.linear_shuffle(self.seq)
        self.seq.sort()
        self.assertEqual(self.seq, range(10))

    def test_linear_shuffle_for_empty_param(self):
        lst = []
        Shuffle.linear_shuffle(lst)
        self.assertEquals(lst, [])
