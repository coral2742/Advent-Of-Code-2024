'''
Challenge: https://adventofcode.com/2024/day/3
By Coral Izquierdo Muñiz with ❤️
'''

import os
import re

current_dir = os.path.dirname(__file__)
file_path = os.path.join(current_dir, "input.txt")

# valid string mul(num1,num2)
expr_mul = "mul\([0-9]+,[0-9]+\)"
mul_list = []

# The do() instruction enables future mul instructions
# The don't() instruction disables future mul instructions
expr_do = "do\(\)"
expr_dont = "don't\(\)"
is_enabled = True



with open(file_path, "r") as f:
    lines = f.readlines()
    #lines = ["xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"]
    for i in range(len(lines)):
        instructions = re.findall(expr_do + "|" + expr_dont + "|" + expr_mul, lines[i])

        for instr in instructions:
            if re.search(expr_do, instr):
                is_enabled = True
            elif re.search(expr_dont, instr):
                is_enabled = False
            elif re.search(expr_mul, instr) and is_enabled:
                mul_list.append(instr)

# multiply
res = 0
for mul in mul_list:
    num1,num2 = re.findall(r'\d+', mul)
    res += int(num1) * int(num2)

print(f"The result is {res}")