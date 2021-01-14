import unittest
from leap_year import LeapYear

class TestLeapYear(unittest.TestCase):

	def test_2000(self):
		ly = LeapYear(2000)
		result = ly.answer()
		self.assertEqual(result,'2000 is a leap year')


	def test_2004(self):
		ly = LeapYear(2004)
		self.assertEqual(ly.answer(),'2004 is a leap year')


	def test_2017(self):
		ly = LeapYear(2017)
		self.assertEqual(ly.answer(),'2017 is a leap year')


	def test_2100(self):
		ly = LeapYear(2100)
		self.assertEqual(ly.answer(),'2100 is a leap year')

if __name__ == '__main__':
	unittest.main()