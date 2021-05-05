from event import Event

class Dialogue:
    def __init__(self, name:str, string:str, id:int, options:list = None, next:int = None, event_to_trigger:Event = None):
        self.name = name
        self.string = string
        self.id = id
        self.options = options
        self.next = next
        self.event_to_trigger = event_to_trigger

    def __str__(self):
        return f'ID: {self.id} {self.name}: {self.string} [Options: {"Yes" if self.options != None else "No"}] [Next: {self.next}]'

    def init_options(self):
        self.options = []

    def add_option(self, option):
        if not self.options:
            self.init_options()
        
        self.options.append(option)

    def get_options(self):
        return self.options
