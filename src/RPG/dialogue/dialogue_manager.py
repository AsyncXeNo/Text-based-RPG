from .dialogue import Dialogue
from .option import Option
from .options_manager import OptionsManager
from .dialogue_utils import get_dialogue
from utils import Logger

logger = Logger('dialogue/dialogue_manager.py')


class DialogueManager:
	def __init__(self):
		self.dialogues_list = list()
		self.current_dialogue_id = None
		self.active = False

		self.options_manager = OptionsManager()

	def activate(self):
		self.active = True

	def deactivate(self):
		self.active = False
		self.dialogues_list = list()
		self.current_dialogue_id = None

	def set_active_dialogue(self, name):
		try:
			self.dialogues_list = get_dialogue(name)
		except:
			logger.log_error(f'no dialogue named {name}.')

		self.set_current_dialogue_id(self.dialogues_list[0]["id"])

	def set_current_dialogue_id(self, id_arg):
		self.current_dialogue_id = id_arg

	def display_dialogue(self, id_arg):
		for dialogue in self.dialogues_list:
			if dialogue['id'] == id_arg:
				logger.custom_log(dialogue['dialogue'], 'bold', 'green')

	def trigger_dialogue(self):

		if self.active:

			self.display_dialogue(self.current_dialogue_id)

			for dialogue in self.dialogues_list:
				if dialogue['id'] == self.current_dialogue_id:
					current_dialogue = dialogue['dialogue']

			if len(self.dialogues_list) == 0:
				logger.log_neutral('No more dialogues.')
				self.deactivate()
				return


			if current_dialogue.options:
				self.options_manager.activate()
				self.options_manager.set_options(current_dialogue.options)
				next_id = self.options_manager.show_options()
				self.current_dialogue_id = next_id
				self.options_manager.deactivate()
				self.trigger_dialogue()
				return 

			else:
				next_id = None
				if current_dialogue.next:
					next_id = current_dialogue.next

			next_dialogue = None

			if next_id != None:
				for dialogue in self.dialogues_list:
					if self.dialogues_list[self.dialogues_list.index(dialogue)]["id"] == next_id:
						next_dialogue = dialogue

			if not (current_dialogue.options == None and current_dialogue.next == None):
				self.current_dialogue_id = self.dialogues_list[self.dialogues_list.index(next_dialogue)]['id']
			
			else:
				logger.log_neutral('Conversation is over. There are no more dialogues.')
				self.deactivate()

		else:			
			logger.log_warning('Dialogue manager is not active.')

