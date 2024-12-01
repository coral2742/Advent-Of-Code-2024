'''
Challenge: https://adventofcode.com/2024/day/1
By Coral Izquierdo Muñiz with ❤️
'''

import os

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

distances = []

for i in range(len(left_list)):
    distance = abs(int(left_list[i]) - int(right_list[i]))
    distances.append(distance)
    
result = sum(distances)

print("The total distance is", result)