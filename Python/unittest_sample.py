import unittest
import sets_example


class ForFun(unittest.TestCase):

    def test_first(self):
        print(sets_example.basket)
        self.assertEqual('foo'.upper(), 'FOO')

    def test_second(self):
        print('Second')
        self.assertTrue('FOO'.isupper())

if __name__ == '__main__':
    unittest.main()

