#!/usr/bin/env python3

import numpy as np


directions = [
    (0, 1),
    (1, 0),
    (0, -1),
    (-1, 0),
]


def find_next_steps(step, matrix):

    next_steps = []

    for direction in directions:

        if (
            0 <= step[0] + direction[0] < matrix.shape[0]
            and 0 <= step[1] + direction[1] < matrix.shape[1]
        ):
            if (
                matrix[step[0] + direction[0]][step[1] + direction[1]]
                == matrix[step[0]][step[1]] + 1
            ):
                next_steps.append([step[0] + direction[0], step[1] + direction[1]])

    return next_steps


def find_trails(trail_head, matrix):

    trail_queue = []
    trail_queue.append([trail_head[0], trail_head[1]])

    visited = []

    trail_ends = set()

    while trail_queue:

        # remove current item from queue and add it to visited
        current_step = trail_queue.pop()
        visited.append(current_step)

        # search for next steps
        next_steps = find_next_steps(current_step, matrix)
        for step in next_steps:

            if matrix[step[0]][step[1]] == 9:
                trail_ends.add((step[0], step[1]))

            if step not in visited and step not in trail_queue:
                trail_queue.append(step)

    return trail_ends


def find_trails_2(trail_head, matrix):

    trail_queue = []
    trail_queue.append([trail_head[0], trail_head[1]])

    visited = []

    trail_ends = []

    while trail_queue:

        # remove current item from queue and add it to visited
        current_step = trail_queue.pop()
        visited.append(current_step)

        # search for next steps
        next_steps = find_next_steps(current_step, matrix)
        for step in next_steps:

            if matrix[step[0]][step[1]] == 9:
                trail_ends.append((step[0], step[1]))

            if step not in trail_queue:
                trail_queue.append(step)

    return trail_ends


def main():

    # read file
    f = open("day10.txt", "r")
    # f = open("day10_test.txt", "r")

    lines = f.read().splitlines()
    matrix = np.array([[int(char) for char in line.rstrip()] for line in lines])
    print(matrix)

    total = 0
    for trail_head in np.argwhere(matrix == 0):
        trail_ends = find_trails(trail_head, matrix)
        total += len(trail_ends)
    print(total)

    total = 0
    for trail_head in np.argwhere(matrix == 0):
        trail_ends = find_trails_2(trail_head, matrix)
        total += len(trail_ends)
    print(total)


if __name__ == "__main__":
    main()
