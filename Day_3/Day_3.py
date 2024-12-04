'''
Challenge: https://adventofcode.com/2024/day/3
By Coral Izquierdo Muñiz with ❤️
'''

import os
import re

current_dir = os.path.dirname(__file__)
file_path = os.path.join(current_dir, "input.txt")

# valid string mul(num1,num2)
expr = "mul\([0-9]+,[0-9]+\)"
mul_list = []

with open(file_path, "r") as f:
    lines = f.readlines()
    for i in range(len(lines)):
        mul_list += re.findall(expr, lines[i])

# multiply
res = 0
for mul in mul_list:
    num1,num2 = re.findall(r'\d+', mul)
    res += int(num1) * int(num2)

print(f"The result is {res}")
