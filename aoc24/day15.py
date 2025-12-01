#!/usr/bin/env python3

from collections import defaultdict
import queue
import numpy as np
from math import floor, ceil
import sys

directions = {
    ">": (0, 1),
    "v": (1, 0),
    "^": (-1, 0),
    "<": (0, -1),
}


def main():

    # read file
    # f = open("day15_test_2.txt", "r")
    f = open("day15.txt", "r")
    # f = open("day14.txt", "r")

    maze, instructions = f.read().split("\n\n")
    instructions = "".join(line.strip() for line in instructions)

    wall = []
    box_positions = {}
    box_ids = {}
    robot = []

    box_id = 0
    for i, line in enumerate(maze.splitlines()):
        for j, char in enumerate(line):

            if char == "O":
                box_positions[box_id] = (i, j)
                box_ids[(i, j)] = box_id
                box_id += 1
            if char == "#":
                wall.append((i, j))
            if char == "@":
                robot = (i, j)

    # print(maze, instructions)
    # print(wall, boxes)

    for instruction in instructions:

        next_position = (
            robot[0] + directions[instruction][0],
            robot[1] + directions[instruction][1],
        )
        # print(instruction)

        # check for wall --> continue
        if next_position in wall:
            # print("hit wall")
            continue

        elif next_position in box_positions.values():
            # print("hit a box")

            boxes_to_update = []
            test_position = next_position
            boxes_to_update.append(
                list(box_positions.keys())[
                    list(box_positions.values()).index(test_position)
                ]
            )

            can_move = True
            while True:
                test_position = (
                    test_position[0] + directions[instruction][0],
                    test_position[1] + directions[instruction][1],
                )

                if test_position in wall:
                    can_move = False
                    break

                elif test_position in box_positions.values():
                    boxes_to_update.append(
                        list(box_positions.keys())[
                            list(box_positions.values()).index(test_position)
                        ]
                    )

                else:
                    break

            if can_move:
                robot = next_position

                # print("hit box, can move")

                for box_id in boxes_to_update:
                    box_positions[box_id] = (
                        box_positions[box_id][0] + directions[instruction][0],
                        box_positions[box_id][1] + directions[instruction][1],
                    )
            # else:
            # print("hit box, can't move")

        else:
            # print("take a step")
            robot = next_position

    #        for i, line in enumerate(maze.splitlines()):
    #            line_str = ""
    #            for j, _ in enumerate(line):
    #
    #                if (i, j) == robot:
    #                    line_str += "@"
    #                elif (i, j) in wall:
    #                    line_str += "#"
    #                elif (i, j) in box_positions.values():
    #                    line_str += "O"
    #                else:
    #                    line_str += "."
    #
    #            print(line_str)

    total = 0
    for x, y in box_positions.values():
        total += 100 * x + y

    print(total)


if __name__ == "__main__":
    main()
