#!/usr/bin/env python3
from collections import defaultdict

answer_size = 0
current_min = 0
space_needed = 0

def get_size(file_tree):

    total_size = 0
    
    for name, content in file_tree.items():
        # if its a file, add to size
        if isinstance(content, int):
            total_size += content
        # if its a directory recurse
        else:
            total_size += get_size(file_tree[name])
            
    if total_size < 100000:
        global answer_size
        answer_size += total_size

    global current_min
    if total_size > space_needed and total_size < current_min:
        current_min = total_size

    return total_size

def main():

    f = open("inputs/day7.txt", "r")
    commands = f.read().split("\n")

    file_tree = defaultdict(dict)
    current_dir = ["/"]

    for command_line in commands:
        split_line = command_line.split(" ")

        if split_line[0] == '$':
            command = split_line[1]

            if command == "cd":
                if split_line[2] == "..":
                    current_dir = current_dir[:-1]
                elif split_line[2] == "/":
                    current_dir = ["/"]
                else:
                    current_dir += [split_line[2]]

        else:

            dic = file_tree
            for key in current_dir:
                dic = dic[key]

            if split_line[0] == "dir":
                dic[split_line[1]] = {}
            else:
                dic[split_line[1]] = int(split_line[0])
    
    total_space = get_size(file_tree)
    print(f"Task 1: {answer_size}")

    unused_space = 70000000 - total_space
    global space_needed
    space_needed = 30000000 - unused_space
    global current_min
    current_min = 921039218032198
    get_size(file_tree)

    print(f"Task 2: {current_min}")


if __name__ == "__main__":
    main()
