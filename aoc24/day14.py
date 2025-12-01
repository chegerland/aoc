#!/usr/bin/env python3

from collections import defaultdict
import queue
import numpy as np
from math import floor, ceil
import sys


def main():

    # read file
    # f = open("day14_test.txt", "r")
    f = open("day14.txt", "r")

    lines = f.read().splitlines()

    positions = {}
    velocities = {}
    for i, line in enumerate(lines):

        p, v = line.split()
        position = np.array([int(x) for x in p.split("=")[-1].split(",")])
        velocity = np.array([int(x) for x in v.split("=")[-1].split(",")])

        positions[i] = position
        velocities[i] = velocity

    width = 101
    height = 103
    quadrants = {
        "ul": [0, floor(width / 2 - 1), 0, floor(height / 2 - 1)],  # ul
        "ur": [ceil(width / 2), width - 1, 0, floor(height / 2 - 1)],  # ur
        "ll": [0, floor(width / 2 - 1), ceil(height / 2), height - 1],  # ll
        "lr": [ceil(width / 2), width - 1, ceil(height / 2), height - 1],  # lr
    }
    quadrant_count = defaultdict(int)

    for step in range(10000):

        input(f"Press Enter to continue...{step}")
        matrix = np.zeros(shape=(width, height))
        for robot_id, position in positions.items():

            positions[robot_id] += velocities[robot_id]

            positions[robot_id] = np.remainder(
                positions[robot_id], np.array([width, height])
            )

            matrix[positions[robot_id][0]][positions[robot_id][1]] = 1
            for quadrant_name, quadrant in quadrants.items():

                if (
                    quadrant[0] <= positions[robot_id][0] <= quadrant[1]
                    and quadrant[2] <= positions[robot_id][1] <= quadrant[3]
                ):
                    quadrant_count[quadrant_name] += 1

        for i in range(width):
            line_str = ""
            for j in range(height):
                if int(matrix[i][j]) == 0:
                    line_str += " "
                else:
                    line_str += "O"
            print(line_str)


#    quadrants = {
#        "ul": [0, floor(width / 2 - 1), 0, floor(height / 2 - 1)],  # ul
#        "ur": [ceil(width / 2), width - 1, 0, floor(height / 2 - 1)],  # ur
#        "ll": [0, floor(width / 2 - 1), ceil(height / 2), height - 1],  # ll
#        "lr": [ceil(width / 2), width - 1, ceil(height / 2), height - 1],  # lr
#    }
#
#    steps = 100
#    quadrant_count = defaultdict(int)
#    for robot_id, position in positions.items():
#
#        positions[robot_id] = position + steps * velocities[robot_id]
#
#        positions[robot_id] = np.remainder(
#            positions[robot_id], np.array([width, height])
#        )
#
#        for quadrant_name, quadrant in quadrants.items():
#
#            if (
#                quadrant[0] <= positions[robot_id][0] <= quadrant[1]
#                and quadrant[2] <= positions[robot_id][1] <= quadrant[3]
#            ):
#                quadrant_count[quadrant_name] += 1
#
#    total = 1
#    for count in quadrant_count.values():
#        total *= count
#
#    print(total)


# print(positions)


if __name__ == "__main__":
    main()
