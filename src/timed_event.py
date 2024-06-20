import copy

class timed_event:
    def __init__(self, lst: list[str]):
        self.department = lst[0]
        self.code = lst[1]
        self.section = lst[2]
        self.lab_section = lst[3]
        self.days: list[str] = []
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



        