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
