#!/usr/bin/python3
def search_replace(my_list, search, replace):
    return list(map(lambda nl: replace if nl == search else nl, my_list))
