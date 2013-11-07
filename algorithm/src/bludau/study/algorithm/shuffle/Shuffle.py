import random

__author__ = 'Anatol Bludau'


class Shuffle(object):

    @classmethod
    def linear_shuffle(cls, lst):
        for i in range(1, len(lst)):
            index_for_switch = random.randrange(0, i)
            lst[i], lst[index_for_switch] = lst[index_for_switch], lst[i]

        return lst