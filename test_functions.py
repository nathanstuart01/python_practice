import unittest
from function_testing import get_formatted_name

class NamesTestCase(unittest.TestCase):
	""" Tests for 'names function ' """

	def test_first_last_name(self):
		formatted_name = get_formatted_name('nathan', 'stuart')
		self.assertEqual(formatted_name, 'Nathan Stuart')

unittest.main()