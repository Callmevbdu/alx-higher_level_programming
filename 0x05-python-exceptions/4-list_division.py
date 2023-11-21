#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    mylist = []

    for x in range(list_length):
        try:
            mylist.append(my_list_1[x] / my_list_2[x])

        except ZeroDivisionError:
            mylist.append(0)
            print('division by 0')
            continue

        except IndexError:
            mylist.append(0)
            print('out of range')
            continue

        except TypeError:
            mylist.append(0)
            print('wrong type')
            continue

        finally:
            pass

    return mylist
