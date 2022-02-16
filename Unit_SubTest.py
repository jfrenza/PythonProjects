import unittest

#The Fuction we want to test

def times_ten(number):
    return number * 100

# Our test class
class TestTimesTen(unittest.TestCase):
    # Atest method
    def test_times_ten(self):
        for num in [0, 1000000, -10]:
            with self.subTest(self):
                expected_result = num * 10
                message = 'Expected times_ten(' + str(num) + ') to return' + str(expected_result)
                self.assertEqual(times_ten(num), expected_result, message)

# Run test
unittest.main()
