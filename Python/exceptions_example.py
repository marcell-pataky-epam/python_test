try:
    print(10 * (1/0))
except ZeroDivisionError:
    print('cannot divide with zero')

try:
    print(4 + spam * 3)
except NameError:
    print('spam variable is not defined')

try:
    print('2' + 2)
except TypeError:
    print('int cannot be converted to string')

try:
    print(10 * (1/0))
except (ZeroDivisionError, NameError, TypeError):
    print('Exception is handled')

import sys

try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
else:
    print('else ...')
    f.close()
finally:
    print('Goodbye, world!')

# raise ValueError('just for fun :)')

print('*' * 40)


def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("division by zero!")
    else:
        print("result is", result)
    finally:
        print("executing finally clause")

# divide(2, 1)
divide(2, 0)
# divide("2", "1")
