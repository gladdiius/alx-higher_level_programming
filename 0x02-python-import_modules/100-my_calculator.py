#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, div, mul
    import sys
    dict = {"+": add, "-": sub, "*": mul, "/": div}
    if (len(sys.argv) - 1) != 3:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        exit(1)
    elif sys.argv[2] not in ['+', '-', '*', '/']:
        print('Unknown operator. Available operators: +, -, * and /')
        exit(1)
    else:
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        print(f'{a} {sys.argv[2]} {b} = {dict[sys.argv[2]](a, b)}')

