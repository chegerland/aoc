#!/usr/bin/env python3

import numpy as np
from collections import defaultdict


def main():

    # read file
    f = open("day6.txt", "r")
    # f = open("day6_test.txt", "r")

    lines = f.read().splitlines()
    matrix = np.array([[char for char in line] for line in lines])
    rotation_matrix = np.array([[0, 1], [-1, 0]])

    visited = np.zeros(matrix.shape)
    guard_position = np.where(matrix == "^")
    start_guard_position = np.where(matrix == "^")

    direction = np.array([-1, 0])

    loops_found = 0

    positions = set()

    while True:
        visited[guard_position] = 1

        # get the next position of the guard
        next_guard_position = (
            guard_position[0] + direction[0],
            guard_position[1] + direction[1],
        )

        # check if out of bounds
        if next_guard_position[0] < 0 or next_guard_position[0] >= matrix.shape[0]:
            break
        if next_guard_position[1] < 0 or next_guard_position[1] >= matrix.shape[1]:
            break

        # check if obstruction
        if matrix[next_guard_position] == "#":
            direction = rotation_matrix.dot(direction)
            continue
        elif not (matrix[next_guard_position] == start_guard_position).all():

            matrix_test = matrix.copy()
            matrix_test[next_guard_position] = "#"
            direction_test = rotation_matrix.dot(direction)
            guard_position_test = guard_position

            positions_dict = defaultdict(int)
            loop_found = False
            while True:
                positions_dict[
                    (guard_position_test[0][0], guard_position_test[1][0])
                ] += 1

                if max(positions_dict.values()) > 10:
                    loop_found = True
                    break

                # get the next position of the guard
                next_guard_position_test = (
                    guard_position_test[0] + direction_test[0],
                    guard_position_test[1] + direction_test[1],
                )

                # check if out of bounds
                if (
                    next_guard_position_test[0] < 0
                    or next_guard_position_test[0] >= matrix_test.shape[0]
                ):
                    break
                if (
                    next_guard_position_test[1] < 0
                    or next_guard_position_test[1] >= matrix_test.shape[1]
                ):
                    break

                # check if obstruction
                if matrix_test[next_guard_position_test] == "#":
                    direction_test = rotation_matrix.dot(direction_test)
                    continue

                guard_position_test = next_guard_position_test

            if loop_found:
                loops_found += 1

        guard_position = next_guard_position

    print(visited.sum())
    print(len(positions))
    print(loops_found)


if __name__ == "__main__":
    main()
