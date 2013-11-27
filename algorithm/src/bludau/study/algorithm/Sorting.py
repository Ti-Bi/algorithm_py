import random

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
            while j > 0 and lst[j - 1] > lst[j]:
                lst[j - 1], lst[j] = lst[j], lst[j - 1]
                j -= 1

        return lst

    @classmethod
    def merge_sort(cls, lst):
        """
        The simple implementation of merge sort.
        :rtype : sorted input list
        :param lst: list for sorting
        """
        if len(lst) <= 1:
            return lst
        else:
            middle = len(lst) // 2
            return cls.__merge(cls.merge_sort(lst[:middle]), cls.merge_sort(lst[middle:]))

    @classmethod
    def quick_sort(cls, lst):
        """
        The simple implementation of quick sort
        :rtype : sorted list (same object with lst)
        :param lst: list for sorting
        """
        #for reduce influence from input
        random.shuffle(lst)

        cls.__quick_sort(lst, 0, len(lst) - 1)

    @classmethod
    def partition(cls, lst, start_index, end_index):
        """
        Separating list on two parts. First element is used as a base element.
        At the result list all of elements witch is less than base place to the left of it
        and witch is greater to the right.
        :rtype : index of the base element in the result or start_index, if there only one element
        :param lst: the list for the partition
        :param start_index: the index from partition will be started (index of the base element)
        :param end_index: the index to partition will be ended
        """
        if end_index <= start_index:
            return start_index
        else:
            base = lst[start_index]
            i = start_index + 1
            j = end_index
            while True:
                while lst[i] < base:
                    i += 1
                    if i >= end_index:
                        break

                while lst[j] > base:
                    j -= 1
                    if j <= start_index:
                        break
                if i >= j:
                    break
                lst[i], lst[j] = lst[j], lst[i]

            lst[start_index], lst[j] = lst[j], lst[start_index]
            return j

    @classmethod
    def __merge(cls, left, right):
        """
        The simple merging of two lists for merge sort.
        :rtype : merged list
        :param left: left part
        :param right: right part
        """
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        result += left[i:]
        result += right[j:]

        return result

    @classmethod
    def __quick_sort(cls, lst, start_index, end_index):
        """
        The recursive implementation of quick sort.
        :rtype : sorted list (same object with lst)
        :param lst: list for sorting
        :param start_index: start index of sub list for sort
        :param end_index: end index of sub list for sort
        """

        if end_index <= start_index:
            return lst
        else:
            middle_index = cls.partition(lst, start_index, end_index)
            cls.__quick_sort(lst, start_index, middle_index - 1)
            cls.__quick_sort(lst, middle_index + 1, end_index)

        return lst
