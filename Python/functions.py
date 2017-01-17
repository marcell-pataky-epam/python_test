def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
    print()

# fib(10000)


def fib_with_return(n=10000):
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a + b
    return result

f10000 = fib_with_return()
# print(f10000)


def book(a):
    print('a')

def book(a,b=1):
    print('a,b')

# book(1)
# book(1, 2)


def cheese_shop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    keys = sorted(keywords.keys())
    for kw in keys:
        print(kw, ":", keywords[kw])

 # cheese_shop("Limburger", "It's very runny, sir.", "It's really very, VERY runny, sir.", shopkeeper="Michael Palin",
 #            client="John Cleese", sketch="Cheese Shop Sketch")


def concat(*args, sep='/'):
    """
    Simple concat function
    :param args: varargs
    :param sep: separator between strings, '/' default separator
    :return: concatenated String
    """
    return sep.join(args)

# print(concat('earth', 'mars', 'venus'))
# print(concat('earth', 'mars', 'venus', sep="."))
print(concat.__doc__)


