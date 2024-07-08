from timed_event import timed_event
from schedule import Schedule

class after_operation:
    def __init__(self):
        self.events = []

    def add_event(self, event: timed_event):
        self.events += [event]

    def __str__(self):
        msg = "Operation: " + str(type(self))
        for event in self.events:
            msg += "\n  " + str(event)

        return msg



class lab_course_match(after_operation):
    def __init__(self):
        self.event = timed_event(["ERR", "ERR", "ERR", "ERR", "_", "ERR", "_", "ERR", "-", "ERR"])

    def add_event(self, event: timed_event):
        if self.event.department == "ERR":
            self.event = event

    def modify_schedule(self, sch: Schedule):
        for e in sch.events:
            if (self.event.department == e.department and 
                    self.event.code == e.code and
                    self.event.section == e.section):
            
                sch.events += [self.event]
                return

    def __str__(self):
        return f"Operation: lab_course_match\n    Event: {str(self.event)}"



        
