#!/usr/bin/python3
def no_c(my_string):
    if not my_string:
        return None
    else:
        croped = ""
        for i in range(len(my_string)):
            if (my_string[i] != 'c' and my_string[i] != 'C'):
                croped += my_string[i]
        return croped

