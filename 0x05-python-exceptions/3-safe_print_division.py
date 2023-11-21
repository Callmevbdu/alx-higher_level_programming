#!/usr/bin/python3
def safe_print_division(a, b):
    SUM = 0

    try:
        return = a / b
    except ZeroDivisionError:
        SUM = None
    finally:
        print('Inside result: {}'.format(SUM))
        return SUM
