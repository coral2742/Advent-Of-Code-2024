'''
Challenge: https://adventofcode.com/2024/day/1
By Coral Izquierdo Muñiz with ❤️
'''

import os
from collections import Counter


current_dir = os.path.dirname(__file__)
file_path = os.path.join(current_dir, "input.txt")

left_list = []
right_list = []

with open(file_path, "r") as f:
    lines = f.readlines()
    for i in range(len(lines)):
        left = lines[i].split()[0]
        right = lines[i].split()[1]
        left_list.append(left)
        right_list.append(right)

left_list.sort()
right_list.sort()

# Dictionary
right_dict = {}

right_dict = Counter(right_list)

result = dict()
sim_score = 0

# for each num in the left list
# if appears in the right list
# multiply the num by the number of times it appears in the right list
for num in left_list:
    if num in right_dict:
        #print(f"Num {num} appears {right_dict[num]} times")
        sim_score += int(num) * right_dict[num]

print("The similarity score is", sim_score)