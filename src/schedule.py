from timed_event import timed_event
from typing import List
import itertools

class Schedule:
    """
    A Schedule is equivivalent to Carleton's worksheets on Carleton Central.
    """

    def __init__(self, events: List[timed_event]):
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
        s = "Schedule(["
        for event in self.events:
            s += f"{repr(event)}, "

        s = s[:-2]

        s += "])"

        return s
    
    def to_yaml(self):
        yaml_str = ""

        # for i in range(len(self.events)):
        #     for j in range(i + 1, len(self.events)):
        #         if (self.events[i].time_conflict_with(self.events[j])):
        remove_events = []
        print("Looking for even/odd lab sections")
        for a, b in itertools.combinations(self.events, 2):
            if (a.time_conflict_with(b, False) and a.lab_section[2] in ['E', 'O'] and b.lab_section[2] in ['E', 'O'] and a.lab_section[2] != b.lab_section[2]):
                yaml_str += self._odd_even_yaml(a, b)
                remove_events += [a, b]

        for event in self.events:
            if event not in remove_events:
                yaml_str += f"{event.to_yaml()}\n"

        return yaml_str
    
    def _odd_even_yaml(self, e1: timed_event, e2: timed_event) -> str:
        #TODO: Current only works if the times are the exact same

        e1_yaml = e1.to_yaml()
        e2_yaml = e2.to_yaml()

        e2_name_index = e2_yaml.find("\n  days: ")
        e2_name = e2_yaml[0:e2_name_index]

        yaml_str = e1_yaml.replace("- name: ", f"{e2_name} / ")

        print(f"yaml_str: {yaml_str}")

        return yaml_str

    