#!/usr/bin/env python3

import numpy as np
from collections import defaultdict


def main():

    # read file
    # f = open("day9.txt", "r")
    f = open("day9_test.txt", "r")

    line = f.read().rstrip()

    blocks = {}

    file_or_space = 0  # zero means file, one means space
    file_position = 0
    file_id = 0

    dense_file_length = 0
    for i, char in enumerate(line):

        file_or_space = i % 2

        if file_or_space == 0:
            for i in range(int(char)):
                blocks[file_position + i] = file_id
            file_id += 1

            dense_file_length += int(char)

        file_position += int(char)

    # print(blocks, file_position, dense_file_length)

    for i in range(dense_file_length - 1):

        # there's already a file
        if i in blocks.keys():
            continue

        # get biggest key
        biggest_key = max(blocks.keys())

        blocks[i] = blocks.pop(biggest_key)

    total = 0
    for position, id in blocks.items():
        total += position * id

    print(total)

    #    # keys are file_ids, value is tuple of file starting position and length
    files = {}

    file_or_space = 0  # zero means file, one means space
    file_position = 0
    file_id = 0
    for i, char in enumerate(line):

        file_or_space = i % 2

        if file_or_space == 0:
            files[file_id] = (file_position, int(char))
            file_id += 1

        file_position += int(char)

    #    print(files, file_id, files[file_id - 1])

    file_size = files[file_id - 1][0]

    print()

    # loop from right indexes to left
    for i in range(file_id - 1, -1, -1):

        # find free space
        sorted_values = sorted(files.values(), key=lambda x: x[0])
        print(i, sorted_values)
        for j in range(1, len(sorted_values)):
            space = (
                sorted_values[j][0] - sorted_values[j - 1][0] - sorted_values[j - 1][1]
            )
            print(
                f"space between {sorted_values[j - 1]} and {sorted_values[j]}: {space}"
            )
            if space >= files[i][1]:
                files[i] = (files[j - 1][0] + files[j - 1][1], files[i][1])
                print(files)
                break

        print()


if __name__ == "__main__":
    main()
