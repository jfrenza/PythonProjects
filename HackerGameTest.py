import unittest
from HackerGame import fizzBuzz

# Test class

class TestfizzBuzz(unittest.TestCase):
    def test_fizz_buzz_3(self):
        self.assertEqual(fizzBuzz(3), [1, 2, 'Fizz'],"Expected HackerGame(3) to return [1, 2, 'Fizz']")

    def test_fizz_buzz_5(self):
        self.assertEqual(fizzBuzz(5), [1, 2, 'Fizz', 4, 'Buzz'],"Expected HackerGame(3) to return [1, 2, 'Fizz', 4, 'Buzz']")

unittest.main()
