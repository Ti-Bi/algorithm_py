__author__ = 'Anatol Bludau'


class StringOperations(object):
    """
    The class includes algorithms, related with string processing.
    """

    @classmethod
    def find_the_largest_palindromic_substring_brut_force(cls, string):
        """
        Finds the larges palindromic substring in input string.
        :param string: string for test
        :return: the largest palindromic substring or None if it isn't exist
        """

        if not string:
            return None

        string_len = len(string)
        if string_len == 1:
            return string

        longest_substring_length = 0
        longest_substring = None

        for i in range(string_len):
            for j in range(i + 1, string_len):
                current_substring_len = j - i
                current_substring = string[i:j+1]
                if cls.is_palindromic_string(current_substring) and current_substring_len > longest_substring_length:
                    longest_substring = current_substring
                    longest_substring_length = current_substring_len

        return longest_substring

    @classmethod
    def find_the_largest_palindromic_substring_matrix(cls, string):
        """
        Finds the larges palindromic substring in input string.
        :param string: string for test
        :return: the largest palindromic substring or None if it isn't exist
        """

        if not string:
            return None

        string_len = len(string)
        if string_len == 1:
            return string

        # create the initial matrix
        matrix = [[0 for i in range(string_len)] for j in range(string_len)]

        # fill matrix
        for i in range(string_len):
            matrix[i][i] = 1

        for i in range(string_len - 1):
            if string[i] == string[i+1]:
                matrix[i][i+1] = 1
                #delete it
                matrix[i+1][i] = 1

        for i in range(string_len-1):
            for j in range(i, string_len):
                if string[i] == string[j]:
                    matrix[i][j] = 1
                    #delete it
                    matrix[j][i] = 1

        longest_string = None
        longest_string_len = 0
        for i in range(string_len):
            start_index = None
            for j in range(i+1):
                current_value = matrix[i-j][j]
                if current_value == 1:
                    if start_index is None:
                        start_index = j
                    if j == i:
                        current_string_len = j - start_index + 1
                        if current_string_len > longest_string_len:
                            longest_string_len = current_string_len
                            longest_string = string[start_index:j+1]
                        start_index = None
                else:
                    if start_index:
                        current_string_len = j - start_index + 1
                        if current_string_len > longest_string_len:
                            longest_string_len = current_string_len
                            longest_string = string[start_index:j]
                        start_index = None

        cls.print_matrix(matrix)
        print longest_string
        return longest_string

    @classmethod
    def print_matrix(cls, matrix):
        for i in matrix:
            print i

    @classmethod
    def is_palindromic_string(cls, string):
        """
        Checks if the input string is palindromic.
        :param string: input string
        :return: True if the input string not empty and palindromic. False in another cases.
        """
        if not string:
            return False

        for i in range(len(string)):
            if string[i] is not string[-i-1]:
                return False

        return True
