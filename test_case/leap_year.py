

#notice : Different indentation will cause unexplainable failure
class LeapYear:
	def __init__(self, year):
		self.year = int(year)

	def answer(self):
		year = self.year
		if year % 100 == 0:
			if year % 400 ==0:
				return'{0} is a leap year'.format(year)
			else:
				return '{0} is not a leap year'.format(year)
		else:
			if year % 4 ==0:
				return '{0} is a leap year'.format(year)
			else:
				return '{0} is not a leap year'.format(year)

