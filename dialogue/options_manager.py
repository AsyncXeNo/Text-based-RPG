class OptionsManager:
	def __init__(self):
		pass

	def show_options(self, options):
		for option in options:
			print (f'{options.index(option) + 1}. option.string')

		while True:
			number = input('type the number of option to choose and press enter.')
			try:
				number = int(number)
			except:
				print('please input a number')
				continue

			if number < 1 or number > len(options):
				print('pls enter a valid option number')
				continue

			else:
				break

		return options[number -1].dialogue_id
