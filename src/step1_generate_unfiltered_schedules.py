#
# Launch this file
#

import os

from timed_event import timed_event
from file_operations import require_all, options_select_one, file_operation
from after_operations import lab_course_match
from schedule import Schedule

filename = 'ErikWinter2026-V1'
# filename = 'ErikWinter2025-TestEvenOdd'

try:
    filepath = os.path.join('src', 'ReadFiles', filename + ".txt")
    file = open(filepath, mode="r")
except Exception as e:
    print ("Failed to open file")
    print ("Exiting program\n")
    print ("Error Message:\n" + str(e))
    exit()

lst_operations = []
lst_after_operations = []

curr_operation = None

for line in file:
    lst = line.split(" ")

    if lst[0] == '':
        lst.pop(0)

    if '#' in lst[0]:
        print("Skipped: " + str(lst))
        continue
    
    if lst[-1] != '\n' and lst[-1].find('\n') != -1:
        lst[-1] = lst[-1].replace('\n', '')
        lst.append('\n')

    # print(lst)


    if lst[0] == '\n':
        if curr_operation != None:
            if isinstance(curr_operation, options_select_one):
                lst_operations += [curr_operation]
                curr_operation = None

            elif isinstance(curr_operation, lab_course_match):
                lst_after_operations += [curr_operation]
                curr_operation = None

            else:
                curr_operation = None
        
        continue

    if lst[0] == 'REQUIRE_ALL':
        curr_operation = require_all()
        continue

    if lst[0] == 'OPTIONS_SELECT_ONE':
        curr_operation = options_select_one()
        continue

    if lst[0] == 'LAB_COURSE_MATCH':
        curr_operation = lab_course_match()
        continue

    if curr_operation != None:
        curr_operation.add_event(timed_event(lst))

file.close()

for elem in lst_operations:
    print (elem)


lst_max_nums = []

for op in lst_operations:
    lst_max_nums += op.get_max()

print(lst_max_nums)

num_permutations = 1
for elem in lst_max_nums:
    num_permutations *= elem

print(num_permutations)

lst_indices = [0] * len(lst_max_nums)
lst_indices_permuations = [tuple(lst_indices)]

for count in range(1, num_permutations):
    i = 0
    check = True
    while check:
        lst_indices[i] += 1

        if lst_indices[i] >= lst_max_nums[i]:
            lst_indices[i] = 0
            i += 1

        else:
            check = False

    lst_indices_permuations += [tuple(lst_indices)]

# safety check
for i in range(0, len(lst_max_nums)):
    if lst_max_nums[i]-1 != lst_indices[i]:
        raise ValueError("Algorithm used from index generator missed some permutations")
    
# safety check
if len(lst_indices_permuations) != len(set(lst_indices_permuations)):
    raise ValueError("A duplicate was created by the index generator")

print("Successful safety check for index generator")

print(len(lst_indices_permuations))


lst_schedules = []
for indices in lst_indices_permuations:
    events = []
    i = 0
    for index in indices:
        events += [lst_operations[i].get(index)]
        i += 1

    lst_schedules += [Schedule(events)]

for op in lst_after_operations:
    print(op)


### Preform after operations
for op in lst_after_operations:
    if isinstance(op, lab_course_match):
        for sch in lst_schedules:
            op.modify_schedule(sch)



try:
    filepath = os.path.join('src', 'Step1-UnfilteredSchedules', filename + ".txt")
    file = open(filepath, mode="w")
    for schedule in lst_schedules:
        file.write(repr(schedule) + "\n")

    file.close()
except Exception as e:
    print ("Failed to write file")
    print ("Exiting program\n")
    print ("Error Message:\n" + str(e))
    exit()

