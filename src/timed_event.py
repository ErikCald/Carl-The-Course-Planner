import copy
from typing import List

class timed_event:
    def __init__(self, lst: List[str]):
        self.department = lst[0]
        self.code = lst[1]
        self.section = lst[2]
        self.lab_section = lst[3]
        self.days: List[str] = []
        self.start_time: str = ""
        self.end_time: str = ""

        while lst[0] != '_':
            lst.pop(0)

        if lst.pop(0) != '_':
            print ("ERROR DECIFERING TIMED EVENT")
        
        while lst[0] != '_':
            self.days += [lst.pop(0)]

        if lst.pop(0) != '_':
            print ("ERROR DECIFERING TIMED EVENT")
        
        self.start_time = lst[0]
        self.end_time = lst[2]

        # print(lst)


    def __str__(self):
        days = ""
        for day in self.days:
            days += day + " "

        return f"{self.department} {self.code} {self.section} {self.lab_section} _ {days}_ {self.start_time} - {self.end_time}"
    
    def __repr__(self):
        return f"timed_event({str(str(self).split(' '))})"
    
    
    def to_yaml(self):
        n = f"{self.department} {self.code} {self.section} {self.lab_section}"

        cap_days = copy.deepcopy(self.days)
        for i in range(0, len(cap_days)):
            cap_days[i] = cap_days[i].capitalize()
            if self.days[i].lower() == 'thu':
                cap_days[i] = 'H'

        d = ', '.join(cap_days)

        return f"- name: {n}\n  days: {d}\n  time: {self.start_time} - {self.end_time}\n"

    def time_conflict_with(self, other_e, ignore_even_odd: bool):
        if ignore_even_odd and len(self.lab_section) > 2 and len(other_e.lab_section) > 2:
            if self.lab_section[2] in ["O", "E"] and other_e.lab_section[2] in ["O", "E"]:
                if self.lab_section[2] != other_e.lab_section[2]:
                    return False

        for i in range(0, len(self.days)):
            self.days[i] = self.days[i].lower()

        for i in range(0, len(other_e.days)):
            other_e.days[i] = other_e.days[i].lower()

        if len(set(self.days) & set(other_e.days)) == 0:
            return False
        
        if self.start_time <= other_e.start_time <= self.end_time:
            return True
        
        if self.start_time <= other_e.end_time <= self.end_time:
            return True
        
        if other_e.start_time <= self.start_time <= other_e.end_time:
            return True
        
        if other_e.start_time <= self.end_time <= other_e.end_time:
            return True
        
        return False
        