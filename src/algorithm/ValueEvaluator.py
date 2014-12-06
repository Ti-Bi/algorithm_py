__author__ = 'Anatol Bludau'


class ValueEvaluator(object):

    __rpn_operators_impl = {
        '+': (lambda a, b: a + b),
        '-': (lambda a, b: a - b),
        '*': (lambda a, b: a * b),
        '/': (lambda a, b: float(a) / b)
    }
    __rpn_operators = ''.join(__rpn_operators_impl.keys())

    @classmethod
    def eval_reverse_polish_notation(cls, str_input):
        """
        This method evaluates the expression given in input string represented as an Reverse Polish Notation.

        :param str_input: input string with reverse polish notation.
        All values and operators should be separated by spaces.
        :return: evaluated value or None if list is empty
        """
        if not str_input:
            return None

    @classmethod
    def eval_reverse_polish_notation_list(cls, list_input):
        """
        This method the same with cls.eval_reverse_polish_notation(), but gets a list as parameter.
        :param list_input:  input list with reverse polish notation.
        :return: evaluated value or None if list is empty
        """

        if not list_input:
            return None

        accepted_operands = "+-*/"

        stack = []

        for token in list_input:
            if type(token) is str and token in accepted_operands:
                val2 = int(stack.pop())
                val1 = int(stack.pop())
                func_for_eval = cls.__rpn_operators_impl[token]
                evaluated_val = func_for_eval(val1, val2)
                stack.append(evaluated_val)
            else:
                stack.append(token)

        return stack.pop()
