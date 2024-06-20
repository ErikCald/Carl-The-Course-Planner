from timed_event import timed_event

class file_operation:
    def __init__(self):
        self.events = []

    def add_event(self, event: timed_event):
        self.events += [event]

    def __str__(self):
        msg = "Operation: " + str(type(self))
        for event in self.events:
            msg += "\n  " + str(event)

        return msg

class options_select_one(file_operation):
    def __init__(self):
        self.events = []

    def get_max(self) -> list[int]:
        return [len(self.events)]
    
    def get(self, index: int) -> timed_event:
        return self.events[index] 

class require_all(file_operation):
    def __init__(self):
        self.events = []

    def get_max(self) -> list[int]:
        return [1] * len(self.events)
