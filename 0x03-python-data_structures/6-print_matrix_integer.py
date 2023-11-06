#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return None
    for submx in matrix:
        if len(submx) == 0:
            print()
        for i in range(len(submx)):
            print("{:d}".format(submx[i]),
                  end="\n" if i is len(submx) - 1 else " ")
