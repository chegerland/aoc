import numpy as np
from math import floor

def read_input(filename):
    lines = []
    with open(filename) as file:
        for line in file:
            # read number line
            chars = [num for num in list(line) if num != '\n']

            lines.append(chars)

    return lines

def check_lines(lines):
    bracket_map = {'[': ']', '(': ')', '{': '}', '<': '>'}
    opening_brackets = bracket_map.keys()

    corrupted_letters = []
    incomplete_lines = []

    for line in lines:
        stack = []
        corrupted = False

        # append opening chars to the stack
        # if a closing char is encountered, pop the last character from the stack
        # if it does not match the line is corrupt
        for char in line:
            if char in opening_brackets:
                stack.append(char)
            else:
                popped = stack.pop()
                if bracket_map[popped] != char:
                    corrupted = True
                    corrupted_letters.append(char)

        # if the line is not corrupted, it is incomplete and we simply get all closing brackets 
        if not corrupted:
            closing_brackets = [bracket_map[bracket] for bracket in reversed(stack)]
            incomplete_lines.append(closing_brackets)

    return incomplete_lines, corrupted_letters

def get_score(corrupted_letters):
    scores = {')': 3, ']': 57, '}': 1197, '>': 25137}
    score = 0

    for letter in corrupted_letters:
        score += scores[letter]

    return score

def get_score_2(incomplete_lines):
    scores = []
    score_map = {')': 1, ']': 2, '}': 3, '>': 4}

    for line in incomplete_lines:
        score = 0
        for char in line:
            score *= 5
            score += score_map[char]
        scores.append(score)
    
    return sorted(scores)[floor(len(scores)/2)]



def main():
    lines = read_input("inputs/day10.txt")
    incomplete_lines, corrupted_letters = check_lines(lines)
    print(get_score(corrupted_letters))
    print(get_score_2(incomplete_lines))


if __name__ == "__main__":
    main()