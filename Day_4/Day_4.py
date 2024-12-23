'''
Challenge: https://adventofcode.com/2024/day/4
By Coral Izquierdo Muñiz with ❤️
'''

import os

def count_horizontal(lines, word):
    count = 0
    for line in lines:
        count += line.count(word)
        count += line[::-1].count(word)
    return count

def count_vertical(lines, word):
    count = 0
    cols = len(lines[0])
    rows = len(lines)
    for col in range(cols):
        column = ''.join(lines[row][col] for row in range(rows))
        count += column.count(word)
        count += column[::-1].count(word)
    return count

# top-left to bottom-right and bottom-right to top-left
def count_diagonal_principal(lines, word):
    count = 0
    rows = len(lines)
    cols = len(lines[0])
    word_length = len(word)

    for start in range(rows + cols - 1):
        diagonal = []
        for row in range(rows):
            col = start - row
            if 0 <= col < cols:
                diagonal.append(lines[row][col])
        diagonal_str = ''.join(diagonal)
        count += diagonal_str.count(word)
        count += diagonal_str[::-1].count(word)

    return count

# top-right to bottom-left and bottom-left to top-right
def count_diagonal_secondary(lines, word):
    count = 0
    rows = len(lines)
    cols = len(lines[0])
    word_length = len(word)


    for start in range(-rows + 1, cols):
        diagonal = []
        for row in range(rows):
            col = start + row
            if 0 <= col < cols:
                diagonal.append(lines[row][col])
        diagonal_str = ''.join(diagonal)
        count += diagonal_str.count(word)
        count += diagonal_str[::-1].count(word)

    return count



current_dir = os.path.dirname(__file__)
file_path = os.path.join(current_dir, "input.txt")

with open(file_path, "r") as f:
    lines = [line.strip() for line in f.readlines()]

# lines = ["MMMSXXMASM", "MSAMXMSMSA", "AMXSXMAAMM", "MSAMASMSMX", "XMASAMXAMM", "XXAMMXXAMA", "SMSMSASXSS", "SAXAMASAAA", "MAMMMXMMMM", "MXMXAXMASX"]
word = "XMAS"
total = 0
total += count_horizontal(lines, word)
total += count_vertical(lines, word)
total += count_diagonal_principal(lines, word)
total += count_diagonal_secondary(lines, word)
print("Number of 'XMAS':", total)
