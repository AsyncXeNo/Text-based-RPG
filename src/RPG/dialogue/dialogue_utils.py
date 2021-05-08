from yaml import load
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

from .option import Option
from .dialogue import Dialogue

with open('res/dialogue/dialogues.yaml') as f:
	dialogues_object = load(f, Loader=Loader)

with open('res/dialogue/options.yaml') as f:
	options_object = load(f, Loader=Loader)


def get_options(name):
	options_list = []
	for option in options_object:
		if option["name"] == name:
			for option_for_individual_dialogue in option["options"]:
				option_id = option_for_individual_dialogue["id"]
				choices = []
				for choice in option_for_individual_dialogue["choices"]:
					choices.append(Option(choice["string"], choice["dialogue"]))

				options_list.append({
					"id": option_id,
					"list": choices
				})

	return options_list

def get_dialogue(name):
	list_of_dialogues = []
	for dialogue in dialogues_object:
		if dialogue["name"] == name:
			for individual_dialogue in dialogue["dialogues"]:

				name = individual_dialogue["name"]
				string = individual_dialogue["string"]
				id_ = individual_dialogue["id"]
				options = individual_dialogue["options"]
				next_dialogue = individual_dialogue["next"]

				options_list = None

				if options != None:
					#print(f'options for dialogue {individual_dialogue["id"]} exist')
					for option in get_options(name):
						if option["id"] == options:
							options_list = option["list"]

				#print(options_list)

				if options_list:
					#print(f'options given to dialogue with id {individual_dialogue["id"]}')
					pass

				list_of_dialogues.append({
					"id": individual_dialogue["id"],
					"dialogue": Dialogue(name, string, id_, options_list, next_dialogue)
				})	

	return list_of_dialogues
