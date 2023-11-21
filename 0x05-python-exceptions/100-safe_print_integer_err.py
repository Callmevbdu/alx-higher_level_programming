#!/usr/bin/python3
import sys
def safe_print_integer_err(value):
    IFint = True
    try:
        print("{:d}".format(value))
    except Exception as ex:
        print("Exception:", ex, file=sys.stderr)
        IFint = False
    return IFint
