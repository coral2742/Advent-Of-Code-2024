'''
Challenge: https://adventofcode.com/2024/day/4
By Coral Izquierdo Muñiz with ❤️
'''

import os

def count_x_mas_patterns(grid):
    total = 0
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    for y in range(rows):
        for x in range(cols):
            if grid[y][x] == "A":
                if (
                    (y > 0 and x > 0 and y < rows - 1 and x < cols - 1) and 
                    (
                        (grid[y - 1][x - 1] == "M" and grid[y + 1][x + 1] == "S") or
                        (grid[y - 1][x - 1] == "S" and grid[y + 1][x + 1] == "M")
                    ) and (
                        (grid[y + 1][x - 1] == "M" and grid[y - 1][x + 1] == "S") or
                        (grid[y + 1][x - 1] == "S" and grid[y - 1][x + 1] == "M")
                    )
                ):
                    total += 1

    return total


example = """.M.S......
..A..MSMS.
.M.S.MAA..
..A.ASMSM.
.M.S.M....
..........
S.S.S.S.S.
.A.A.A.A..
M.M.M.M.M.
.........."""


current_dir = os.path.dirname(__file__)
file_path = os.path.join(current_dir, "input.txt")

with open(file_path, "r") as f:
    lines = [list(line.strip()) for line in f.readlines()]

#lines = [list(line) for line in example.strip().splitlines()]
#result = count_x_mas_patterns(lines)
result = count_x_mas_patterns(lines)
print("Number of MAS:", result)
