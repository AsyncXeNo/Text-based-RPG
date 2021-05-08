from utils import Logger

logger = Logger('dialogue/options_manager.py')


class OptionsManager:
	def __init__(self):
		self.active = False
		self.options = []

	def activate(self):
		self.active = True

	def deactivate(self):
		self.active = False
		self.options = []

	def set_options(self, options):
		self.options = options

	def show_options(self):
		for option in self.options:
			logger.custom_log(f'{self.options.index(option) + 1}. {option.string}', 'bold', 'green')

		while True:
			logger.custom_log('type the number of option to choose and press enter.', 'bold', 'green')
			number = input()
			try:
				number = int(number)
			except:
				logger.log_error('please input a number')
				continue

			if number < 1 or number > len(self.options):
				logger.log_error('pls enter a valid option number')
				continue

			else:
				break

		return self.options[number -1].dialogue_id