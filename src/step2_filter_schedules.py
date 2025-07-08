#
# Launch this file
#

import os, typing
from collections.abc import Callable
from typing import Any

from timed_event import timed_event
from file_operations import require_all, options_select_one, file_operation
from schedule import Schedule
import filters

# filename = 'ErikWinter2025-TestEvenOdd'
filename = 'ErikWinter2026-V1'
filter_name = 'unfilteredV1'

lst_schedules: typing.List[Schedule] = []
try:
    filepath = os.path.join('src', 'Step1-UnfilteredSchedules', filename + ".txt")
    file = open(filepath, mode="r")
    
except Exception as e:
    print ("Failed to open file")
    print ("Exiting program\n")
    print ("Error Message:\n" + str(e))
    exit()

try:
    for line in file:
        lst_schedules += [eval(line)]

except Exception as e:
    print ("Failed to reconstruct schedules")
    print ("Exiting program\n")
    print ("Error Message:\n" + str(e))
    exit()

file.close()

def filter(name: str, bool_func: typing.Callable[[Schedule, Any], bool], extra: Any):
    print(f"Applying filter: {name} \nPermutations before: {len(lst_schedules)}\n")

    i = 0
    while i < len(lst_schedules):
        if bool_func(lst_schedules[i], extra):
            removed = lst_schedules.pop(i)
            # print(f"Removing: {str(removed)}")
            continue
        i += 1

    print(f"Permutations after: {len(lst_schedules)}\n\n")

## MUST HAVE
filter("Matching lab and course sections", filters.has_mismatching_labcourse_section, "")
filter("Time conflicts", filters.has_time_conflicts, "")
## MUST HAVE


# before_time = "10:00"
# filter(f"Remove courses that start before {before_time}", filters.has_morning_course, before_time)

# filter("Must have a spare day", filters.has_no_spare_day, "")

# filter("Must have a semi spare day", filters.has_no_semispare_day, 1)

# wait_time = 6*60
# filter(f"Must have no wait time of more than {wait_time} minutes", filters.has_wait_time, wait_time)

# max_carl_time = 26
# filter(f"Must have a carl time of less than {max_carl_time} hours", filters.has_total_carl_time, max_carl_time)

try:
    filepath = os.path.join('src', 'Step2-filteredSchedules', f"{filename}-{filter_name}.txt")
    file = open(filepath, mode="w")
    for schedule in lst_schedules:
        file.write(repr(schedule) + "\n")

    file.close()
except Exception as e:
    print ("Failed to write file")
    print ("Exiting program\n")
    print ("Error Message:\n" + str(e))
    exit()











# def change_day(s):
#     if s == 'mon':
#         return '1mon'
        
#     elif s == '1mon':
#         return 'mon'

#     elif s == 'tue':
#         return '2tue'
            
#     elif s == '2tue':
#         return 'tue'

#     elif s == 'wed':
#         return '3wed'
            
#     elif s == '3wed':
#         return 'wed'

#     elif s == '4thu':
#         return 'thu'
            
#     elif s == 'thu':
#         return '4thu'

#     elif s == '5fri':
#         return 'fri'
            
#     elif s == 'fri':
#         return '5fri'


# for sch in lst_schedules:
#     for i in range(0, len(sch.events)):
#         for j in range(0, len(sch.events[i].days)):
#             s = sch.events[i].days[j] 
#             if s == 'mon':
#                 s = '1mon'
                
#             elif s == '1mon':
#                 s = 'mon'

#             elif s == 'tue':
#                 s = '2tue'
                    
#             elif s == '2tue':
#                 s = 'tue'

#             elif s == 'wed':
#                 s = '3wed'
                    
#             elif s == '3wed':
#                 s = 'wed'

#             elif s == 'thu':
#                 s = '4thu'
                    
#             elif s == '4thu':
#                 s = 'thu'

#             elif s == 'fri':
#                 s = '5fri'
                    
#             elif s == '5fri':
#                 s = 'fri'

#             sch.events[i].days[j] = s

#     # for event in sch.events:
#     #     for i in range(0, len(event.days)):
#     #         s = change_day(event.days[i])
#     #         event.days[i] = s


    
#     # for i in range(0, len(sch.events)):
#     #     for j in range(0, len(sch.events[i].days)):
#     #         sch.events[i].days[j] = change_day(sch.events[i].days[j])


#     sch.events.sort(key=lambda x: (x.days, x.start_time))

#     for i in range(0, len(sch.events)):
#         for j in range(0, len(sch.events[i].days)):
#             s = sch.events[i].days[j] 
#             if s == 'mon':
#                 s = '1mon'
                
#             elif s == '1mon':
#                 s = 'mon'

#             elif s == 'tue':
#                 s = '2tue'
                    
#             elif s == '2tue':
#                 s = 'tue'

#             elif s == 'wed':
#                 s = '3wed'
                    
#             elif s == '3wed':
#                 s = 'wed'

#             elif s == 'thu':
#                 s = '4thu'
                    
#             elif s == '4thu':
#                 s = 'thu'

#             elif s == 'fri':
#                 s = '5fri'
                    
#             elif s == '5fri':
#                 s = 'fri'

#             sch.events[i].days[j] = s


# try:
#     filepath = os.path.join('src', 'Step2-filteredSchedules', filename + "-clean.txt")
#     file = open(filepath, mode="w")
#     for schedule in lst_schedules:
#         file.write(str(schedule) + "\n")

#     file.close()
# except Exception as e:
#     print ("Failed to write file")
#     print ("Exiting program\n")
#     print ("Error Message:\n" + str(e))
#     exit()

