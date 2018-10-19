class WeatherSearch(object):
	"""docstring for WeatherSearch"""
	def __init__(self, input_daytime):
		self.input_daytime = input_daytime

	def seach_visibility(self):
		visible_leave = 0
		if self.input_daytime == 'daytime':
			visible_leave = 2
		elif self.input_daytime == 'night':
			visible_leave == 9
		return visible_leave

	def seach_temperature(self):
		temperature = 0
		if self.input_daytime == 'daytime':
			temperature = 26
		elif self.input_daytime == 'night':
			temperature = 16
			return temperature


class OutAdvice(WeatherSearch):
	def __init__(self, input_daytime):
		WeatherSearch.__init__(self, input_daytime)

	def seach_temperature(self):
		vehicle = ''
		if self.input_daytime == 'daytime':
			vehicle = 'bike'
		elif self.input_daytime == 'night':
			vehicle = 'taxi'
		return vehicle

	def out_advice(self):
		visible_leave = self.seach_visibility()
		if visible_leave == 2:
			print('The weather is goog,suitable for use %s.' % self.seach_temperature())
		elif visible_leave == 9:
			print('The weather is bad,you should use %s.' % self.seach_temperature())
		else:
			print('The weather is beyond my scope,I can not give you any advices')

check = OutAdvice('daytime')
check.out_advice()
