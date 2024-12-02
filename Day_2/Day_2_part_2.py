'''
Challenge: https://adventofcode.com/2024/day/2
By Coral Izquierdo Muñiz with ❤️
'''

import os

current_dir = os.path.dirname(__file__)
file_path = os.path.join(current_dir, "input.txt")

safe_reports = 0

# A report is safe if:
# - The levels are either all increasing or all decreasing
# - Any two adjacent levels differ by at least one and at most three  
def is_safe(report):
    dif = 0
    is_increasing = True
    prev = int(report.split()[0])
    next = int(report.split()[1])
    # check if the levels are increasing or decreasing
    if prev < next:
        is_increasing = True
    elif prev > next:
        is_increasing = False
        
    for i in range(len(report.split()) - 1):
        prev = int(report.split()[i])
        next = int(report.split()[i + 1])
        # check if the levels are still increasing or decreasing
        if is_increasing and prev > next:
            #print(f"Report {report} is not safe")
            return False
        elif not is_increasing and prev < next:
            #print(f"Report {report} is not safe")
            return False
        
        dif = abs(prev - next)
        if dif < 1 or dif > 3:
            #print(f"Report {report} is not safe")
            return False
    #print(f"Report {report} is safe")
    return True


# A report is also safe if it is safe after removing one level
def check_without_level(report):
    levels = report.split()
    
    if (is_safe(report)):
        return True
    else:
        for i in range(len(levels)):
            new_report = " ".join(levels[:i] + levels[i+1:])
            if is_safe(new_report):
                return True
    return False

with open(file_path, "r") as f:
    lines = f.readlines()
    
    # Example
    """
    lines = ["7 6 4 2 1",
            "1 2 7 8 9",
            "9 7 6 2 1",
            "1 3 2 4 5",
            "8 6 4 4 1",
            "1 3 6 7 9"]
    """
    for i in range(len(lines)):
        if check_without_level(lines[i]):
            safe_reports += 1
        
   
print(f"The number of safe reports is {safe_reports}")