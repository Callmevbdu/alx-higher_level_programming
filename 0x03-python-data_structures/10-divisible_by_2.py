#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list is None:
        return None

    divisions = []

    for i in my_list:
        if (i % 2) == 0:
            divisions.append(True)
        else:
            divisions.append(False)

    return divisions
