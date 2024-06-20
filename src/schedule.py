from timed_event import timed_event

class schedule:
    """
    A Schedule is equivivalent to Carleton's worksheets on Carleton Central.
    """

    def __init__(self, events: list[timed_event]):
        self.events = events

    def num(self):
        return len(self.events)

    def __str__(self):
        s = "Schedule:\n"
        for event in self.events:
            s += f"  {str(event)}\n"
        return s
    
    # NOTE: eval()
    def __repr__(self):
        s = "schedule(["
        for event in self.events:
            s += f"{repr(event)}, "

        s = s[:-2]

        s += "])"

        return s
    

    def to_yaml(self):
        str = ""
        for event in self.events:
            str += f"{event.to_yaml()}\n"

        return str

    