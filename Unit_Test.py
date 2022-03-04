import unittest

#Function to test

def times_ten(number):
    return number * 100

#Test class class

class TestTimesTen(unittest.TestCase):
    def test_multiply_ten_by_zero(self):
        self.assertEqual(times_ten(0), 0, 'Expected times_ten(0) to return 0')

    def test_multiply_ten_by_ten(self):
        self.assertEqual(times_ten(10), 100, 'Expected times_ten(10) to return 100')

    def test_multiply_ten_by_minusten(self):
        self.assertEqual(times_ten(-10), -100, 'Expected times_ten(-10) to return -100')

#Run the Test

unittest.main()
