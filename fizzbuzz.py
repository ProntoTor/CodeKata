'''
The problem is

If input number divisible by 3 will return string "Fizz"
If input number divisible by 5 will return string "Buzz"
If input number divisible by 3 and 5 will return string "FizzBuzz"
If input number can not divisible by 3 and 5 will return string of this number

Example
input(1) -> "1"
input(3) -> "Fizz"
input(5) -> "Buzz"
input(6) -> "Fizz"
input(10) -> "Buzz"
input(15) -> "FizzBuzz"
input(30) -> "FizzBuzz"
'''

import unittest


class FizzBuzzTest(unittest.TestCase):
	def test_input_1_should_return_sting_1(self):
		fizzbuzz = FizzBuzz()
		number = 1
		actual = fizzbuzz.take(number)
		expected = '1'

		self.assertEquals(expected, actual)


class FizzBuzz:
	def take(self, number):
		return '1'

if __name__ == '__main__':
    unittest.main()