
class Logger():
    
	def __init__(self):
		self.escape_code = '\033['
		self.end_escape = 'm'

		self.colors = {
			None: 37,
			'black': 30,
			'red': 31,
			'green': 32,
			'yellow': 33,
			'blue': 34,
			'purple': 35,
			'cyan': 36,
			'white': 37
		}

		self.styles = {
			None: 0,
			'bold': 1,
			'underline': 2,
			'negative1': 3,
			'negative2': 5
		}

		self.levels = {'neutral': 1, 'warning': 2, 'alert': 3, 'error': 4}

		self.log_functions = {
			1: self.log_neutral,
			2: self.log_warning,
			3: self.log_alert,
			4: self.log_error,
		}

		self.end = f'{self.escape_code}{self.styles[None]};{self.colors[None]}{self.end_escape}'


	def log(self, msg, level):
		self.log_functions[self.levels[level]](msg)


	def log_neutral(self, msg):
		msg_style = self.styles[None]
		msg_color = self.colors['green']

		loginfo = 'NORMAL '

		self.display(loginfo, msg, msg_style, msg_color)

	def log_warning(self, msg):
		msg_style = self.styles['underline']
		msg_color = self.colors['yellow']
		
		loginfo = 'WARNING'

		self.display(loginfo, msg, msg_style, msg_color)

	def log_alert(self, msg):
		msg_style = self.styles[None]
		msg_color = self.colors['yellow']

		loginfo = 'ALERT'

		self.display(loginfo, msg, msg_style, msg_color)