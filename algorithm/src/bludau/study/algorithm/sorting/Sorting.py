__author__ = 'Anatol Bludau'


class Sorting(object):
    @classmethod
    def selection_sort(cls, lst):
        """
        The simple implementation of selection sort.
        :rtype : sorted input list
        :param lst: list for sorting
        """
        for i in range(len(lst)):
            min_index = i
            min_element = lst[i]
            for j in range(i + 1, len(lst)):
                if lst[j] < min_element:
                    min_element = lst[j]
                    min_index = j

            # exchange the elements
            lst[i], lst[min_index] = lst[min_index], lst[i]

        return lst