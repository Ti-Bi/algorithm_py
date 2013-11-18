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

    @classmethod
    def insertion_sort(cls, lst):
        """
        The simple implementation of insertion sort.
        :rtype : sorted input list
        :param lst: list for sorting
        """
        for i in range(1, len(lst)):
            j = i
            while j > 0 and lst[j-1] > lst[j]:
                lst[j-1], lst[j] = lst[j], lst[j-1]
                j -= 1

        return lst

    @classmethod
    def merge_sort(cls, lst):
        """
        The simple implementation of merge sort.
        :rtype : sorted input list
        :param lst: list for sorting
        """
        temp_lst = list(lst)
        cls.__merge_sort(lst, temp_lst)

    @classmethod
    def __merge_sort(cls, lst, temp_lst, start, end):
        lstt = list(lst)
        lstt.