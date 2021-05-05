from dialogue import Dialogue
from option import Option
from options_manager import OptionsManager
from utils import get_dialogue


class DialogueManager:
	def __init__(self):
		self.dialogues_list = list()
		self.current_dialogue = None
		self.active = False

		self.options_manager = OptionsManager()

	def activate(self):
		self.active = True

	def deactivate(self):
		self.active = False
		self.dialogues_list = list()
		self.current_dialogue = False

	def set_active_dialogue(self, name):
		try:
			self.dialogues_list = get_dialogue(name)
		except:
			print(f'no dialogue named {name}.')

		self.current_dialogue = self.dialogues_list.pop(0)["dialogue"]

	def trigger_dialogue(self):
		if self.active:

			print(self.dialogues_list)
			if len(self.dialogues_list) == 0:
				print('no more dialogues')
				self.deactivate()
				return


			if self.current_dialogue.options:
				next_dialogue_id = self.options_manager.show_options(self.current_dialogue.options)
			else:
				next_dialogue_id = self.current_dialogue.next

			next_dialogue = None
			for dialogue in range(len(self.dialogues_list)):
				if self.dialogues_list[dialogue]["id"] == next_dialogue_id:
					next_dialogue = dialogue

			if next_dialogue == None:
				print('something went wrong')

			self.current_dialogue = self.dialogues_list.pop(next_dialogue)["dialogue"]
		else:
			
			print('dialogue manager is not active')

