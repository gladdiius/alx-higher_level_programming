#!/usr/bin/python3
def safe_print_integer(value):
    import sys
    try:
        print("{:d}".format(value))
    except (ValueError, TypeError):
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return False
    return True
