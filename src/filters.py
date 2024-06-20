from datetime import datetime

from schedule import schedule
from timed_event import timed_event

# Check if a schedule has mismatched course and lab sections
def has_mismatching_labcourse_section(sch: schedule, dummy) -> bool:
    for event in sch.events:
        if len(event.lab_section) > 1 and event.lab_section[0] != "L":
            for event2 in sch.events:
                if event != event2 and event.department == event2.department and event.code == event2.code and event.section != event2.section:
                    return True
    return False

# Check if a schedule has time conflicts
def has_time_conflicts(sch: schedule, dummy) -> bool:
    for i in range(len(sch.events)):
        for j in range(i + 1, len(sch.events)):
            if _is_time_conflict(sch.events[i], sch.events[j]):
                return True

    return False

def _is_time_conflict(e1: timed_event, e2: timed_event):
    if len(e1.lab_section) > 2 and len(e2.lab_section) > 2:
        if e1.lab_section[2] in ["O", "E"] and e2.lab_section in ["O", "E"]:
            if e1.lab_section[2] != e2.lab_section[2]:
                print(f"Odd/even lab section, E1: {str(e1)}, E2: {str(e2)}")
                return False

    for i in range(0, len(e1.days)):
        e1.days[i] = e1.days[i].lower()

    for i in range(0, len(e2.days)):
        e2.days[i] = e2.days[i].lower()

    if len(set(e1.days) & set(e2.days)) == 0:
        return False
    
    if e1.start_time <= e2.start_time <= e1.end_time:
        return True
    
    if e1.start_time <= e2.end_time <= e1.end_time:
        return True
    
    if e2.start_time <= e1.start_time <= e2.end_time:
        return True
    
    if e2.start_time <= e1.end_time <= e2.end_time:
        return True
    
    return False


# Filter Mornings
def has_morning_course(sch: schedule, before_time) -> bool:
    for e in sch.events:
        if e.start_time < before_time:
            return True
        
    return False


# Filter: Remove all schedules that have no free day
def has_no_spare_day(sch: schedule, dummy) -> bool:
    all_days = set()
    for e in sch.events:
        for day in e.days:
            all_days.add(day.lower())

    if len(all_days) == 5:
        return True
    
    return False

# Filter: Remove all schedules that have no semi-free day
def has_no_semispare_day(sch: schedule, num_on_one_day: int) -> bool:
    d = {"mon": 0, "tue": 0, "wed": 0, "thu": 0, "fri": 0}
    for e in sch.events:
        for day in e.days:
            d[day.lower()] += 1

    for value in d.values():
        if value <= num_on_one_day:
            return False
        
    return True


# Filter: Remove all schedules with a wait time at carleton
def has_wait_time(sch: schedule, max_wait_time_minutes: int) -> bool:
    FMT = '%H:%M'

    d = {"mon": [], "tue": [], "wed": [], "thu": [], "fri": []}
    for e in sch.events:
        tuple = (datetime.strptime(e.start_time, FMT), 
                 datetime.strptime(e.end_time, FMT))

        for day in e.days:
            d[day.lower()] += [tuple]

    for day in d.values():
        day.sort()

    for day in d.values():
        for i in range(0, len(day)-1):
            tdelta = day[i+1][0] - day[i][1]
            if tdelta.seconds/60.0 > max_wait_time_minutes:
                return True

    return False

# Filter: Reduce time spent at carleton
def has_total_carl_time(sch: schedule, max_carl_time_hours: int) -> bool:
    FMT = '%H:%M'

    d = {"mon": [], "tue": [], "wed": [], "thu": [], "fri": []}
    for e in sch.events:
        tuple = (datetime.strptime(e.start_time, FMT), 
                 datetime.strptime(e.end_time, FMT), e.lab_section != "C")

        for day in e.days:
            d[day.lower()] += [tuple]

    for day in d.values():
        day.sort()

    total_carl_time = 0
    for day in d.values():
        if len(day) != 0:
            total_carl_time += (day[len(day)-1][1] - day[0][0]).seconds/60.0/60.0

        if day[len(day)-1][2] == True:
            total_carl_time -= 1

        
    if total_carl_time > max_carl_time_hours:
        return True

    return False



# sch = schedule([timed_event(['SYSC', '3110', 'A', 'C', '_', 'wed', 'fri', '_', '13:05', '-', '14:25']), timed_event(['SYSC', '3110', 'A', 'L4', '_', 'mon', '_', '14:35', '-', '17:25']), timed_event(['SYSC', '3120', 'A', 'C', '_', 'wed', 'fri', '_', '11:35', '-', '12:55']), timed_event(['SYSC', '3120', 'A', 'L4O', '_', 'tue', '_', '14:35', '-', '17:25']), timed_event(['SYSC', '3310', 'A', 'C', '_', 'mon', 'wed', '_', '18:05', '-', '19:25']), timed_event(['SYSC', '3310', 'A', 'A2', '_', 'tue', '_', '11:35', '-', '13:25']), timed_event(['SYSC', '4001', 'B', 'C', '_', 'tue', 'thu', '_', '10:05', '-', '11:25']), timed_event(['SYSC', '4001', 'B', 'B2', '_', 'thu', '_', '14:35', '-', '17:25']), timed_event(['COMP', '3005', 'B', 'C', '_', 'mon', 'wed', '_', '10:05', '-', '11:25'])])
# print(has_wait_time(sch, 4*60))