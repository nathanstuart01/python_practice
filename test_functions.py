import unittest
from function_testing import get_formatted_name

class NamesTestCase(unittest.TestCase):
	""" Tests for 'names function ' """

	def test_first_last_name(self):
		formatted_name = get_formatted_name('nathan', 'stuart')
		self.assertEqual(formatted_name, 'Nathan Stuart')

	def test_first_last_middle_name(self):
		formatted_name = get_formatted_name(
			'wolfgang', 'mozart', 'amadeus')
		self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')

unittest.main()