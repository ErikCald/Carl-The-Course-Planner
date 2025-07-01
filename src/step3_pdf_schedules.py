#
# Launch this file
#

import os
from collections.abc import Callable
from typing import List

from timed_event import timed_event
from file_operations import require_all, options_select_one, file_operation
from schedule import Schedule

filename = 'ErikFall2025-V1'
filter_name = 'unfilteredV1'

filename = f"{filename}-{filter_name}"

lst_schedules: List[Schedule] = []
try:
    filepath = os.path.join('src', 'Step2-filteredSchedules', filename + ".txt")
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
try:
    dirpath = os.path.join('src', 'Step3-PDFSchedules', f"{filename}")
    os.mkdir(dirpath)
except:
    print("Folder already created")

try:
    dirpath = os.path.join('src', 'Step3-PDFSchedules', f"{filename}", f"{filename}-ymls")
    os.mkdir(dirpath)
except:
    print("Folder already created")

try:
    dirpath = os.path.join('src', 'Step3-PDFSchedules', f"{filename}", f"{filename}-pdfs")
    os.mkdir(dirpath)
except:
    print("Folder already created")


i = 0
for sch in lst_schedules:
    i += 1
    schymlpath = os.path.join('src', 'Step3-PDFSchedules', f"{filename}", f"{filename}-ymls", f"{filename}-{i}.yml")
    schpdfpath = os.path.join('src', 'Step3-PDFSchedules', f"{filename}", f"{filename}-pdfs", f"{filename}-{i}.pdf")

    file = open(schymlpath, mode="w")
    file.write(sch.to_yaml())
    file.close()

    os.system(f"pdfschedule {schymlpath} {schpdfpath}")    
