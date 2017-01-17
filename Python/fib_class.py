class FibClass:

    """Simple class to calculate Fibonacci numbers"""

    def __init__(self):
        self.a, self.b = 0, 1
        self.result = []

    def fib(self, n):  # return Fibonacci series up to n
        while self.b < n:
            self.result.append(self.b)
            self.a, self.b = self.b, self.a + self.b
        return self.result

