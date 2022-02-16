import unittest

#Function to test

def times_ten(number):
    return number * 100

#Test class class

class TestTimesTen(unittest.TestCase):
    def test_multiply_ten_by_zero(self):
        self.assertEqual(times_ten(0), 0, 'Expected times_ten(0) to return 0')

#Run the Test

unittest.main()
print('hello word')
