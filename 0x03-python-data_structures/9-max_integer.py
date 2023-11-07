#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) < 1:
        return None
    copyList = my_list.copy()
    copyList.reverse()
    return copyList[0]
