__author__ = 'anatolbludau'


class MatrixBypass(object):

    __simple_print = lambda x: print(str(x), end="\t")
    __print_new_line = lambda x: print()

    @classmethod
    def simple(cls, matrix, on_row=__print_new_line, on_element=__simple_print):
        if not matrix:
            return

        for i in matrix:
            for j in i:
                on_element(j)
            on_row(i)
