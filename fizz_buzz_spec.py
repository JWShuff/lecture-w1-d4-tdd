from fizz_buzz import fizz_buzz, fizz_buzz_N, blah_yah_generic_N
import unittest # imports the Unit Test library

class FizzbuzzTestCase(unittest.TestCase):
    """Tests for `fizz_buzz.py`."""

    def test_returns_a_list(self):
        """When you call fizz buzz(), you should get a list back"""
        self.assertIsInstance(fizz_buzz(), list)

    def test_returns_100_elements(self):
        """
        Verify that exactly 100 elements are returned from fizz_buzz()
        """
        returned_list = fizz_buzz()
        elements = len(returned_list)
        self.assertEqual(elements, 100)

    def test_fizzy_and_buzzy(self):
        """
        Verify that "Fizz" and "Buzz" and "Fizzbuzz" are output in appropriate places
        in our list 
        """
        actual_output = fizz_buzz()
        expected_output = [1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz", 11, "Fizz", 13, 14, "Fizzbuzz", 16, 17, "Fizz", 19, "Buzz", "Fizz", 22, 23, "Fizz", "Buzz", 26, "Fizz", 28, 29, "Fizzbuzz", 31, 32, "Fizz", 34, "Buzz", "Fizz", 37, 38, "Fizz", "Buzz", 41, "Fizz", 43, 44, "Fizzbuzz", 46, 47, "Fizz", 49, "Buzz", "Fizz", 52, 53, "Fizz", "Buzz", 56, "Fizz", 58, 59, "Fizzbuzz", 61, 62, "Fizz", 64, "Buzz", "Fizz", 67, 68, "Fizz", "Buzz", 71, "Fizz", 73, 74, "Fizzbuzz", 76, 77, "Fizz", 79, "Buzz","Fizz", 82, 83, "Fizz", "Buzz", 86, "Fizz", 88, 89, "Fizzbuzz", 91, 92, "Fizz", 94, "Buzz", "Fizz", 97, 98, "Fizz", "Buzz"]

        self.assertListEqual(actual_output, expected_output)

    def test_fizz_buzz_for_25_value(self):
        """
        Verify that "Fizz" and "Buzz" and "Fizzbuzz" are output in appropriate places
        in our list with 25 elements
        """
        actual_output = fizz_buzz_N(25)
        expected_output = [1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz", 11, "Fizz", 13, 14, "Fizzbuzz", 16, 17, "Fizz", 19, "Buzz", "Fizz", 22, 23, "Fizz", "Buzz"]

        self.assertListEqual(actual_output, expected_output)

    def test_fizz_buzz_for_0_value(self):
        """
        Verify that "Fizz" and "Buzz" and "Fizzbuzz" are output in appropriate places
        in our list with 0 elements
        """
        actual_output = fizz_buzz_N(0)
        expected_output = []

        self.assertListEqual(actual_output, expected_output)

    def test_blah_yah_for_25_value(self):
        """
        Verify that "Fizz" and "Buzz" and "Fizzbuzz" are output in appropriate places
        in our list with 0 elements
        """

        actual_output = blah_yah_generic_N(25, "donuts", "cookies", "sugar coma")
        expected_output = [1, 2, "donuts", 4, "cookies", "donuts", 7, 8, "donuts", "cookies", 11, "donuts", 13, 14, "sugar coma", 16, 17, "donuts", 19, "cookies", "donuts", 22, 23, "donuts", "cookies"]

        self.assertListEqual(actual_output, expected_output)


if __name__ == '__main__':
    unittest.main()
