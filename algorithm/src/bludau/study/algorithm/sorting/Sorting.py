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

    @classmethod
    def partition(cls, lst, start_index, end_index):
        """
        Separating list on two parts. First element is used as a base element.
        At the result list all of elements witch is less than base place to the left of it
        and witch is greater to the right.
        :rtype : index of the base element in the result
        :param lst: the list for the partition
        :param start_index: the index from partition will be started (index of the base element)
        :param end_index: the index to partition will be ended
        """
        base = lst[start_index]
        i = start_index + 1
        j = end_index
        while True:
            while lst[i] < base:
                i += 1
                if i == end_index:
                    break

            while lst[j] > base:
                j -= 1
                if j == start_index:
                    break

            if i >= j:
                break
            lst[i], lst[j] = lst[j], lst[i]
        pass
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
