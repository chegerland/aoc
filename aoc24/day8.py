#!/usr/bin/env python3

import numpy as np
from collections import defaultdict


def main():

    # read file
    # f = open("day7.txt", "r")
    f = open("day8_test_2.txt", "r")
    # f = open("day8.txt", "r")

    lines = f.read().splitlines()

    antennas = defaultdict(list)

    width = len(lines[0])
    height = len(lines)
    print(width, height)
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if char != ".":

                antennas[char].append((i, j))

    antinodes = set()
    for antenna_type, locations in antennas.items():

        for location1 in locations:
            for location2 in locations:

                if location1 != location2:

                    direction = (
                        location1[0] - location2[0],
                        location1[1] - location2[1],
                    )

                    antinode1 = (
                        location1[0] + direction[0],
                        location1[1] + direction[1],
                    )
                    antinode2 = (
                        location2[0] - direction[0],
                        location2[1] - direction[1],
                    )

                    if (
                        0 <= antinode1[0] <= height - 1
                        and 0 <= antinode1[1] <= width - 1
                    ):
                        antinodes.add(antinode1)

                    if (
                        0 <= antinode2[0] <= height - 1
                        and 0 <= antinode2[1] <= width - 1
                    ):
                        antinodes.add(antinode2)

    #    print(antinodes)
    print(len(antinodes))

    antinodes = set()
    for _, locations in antennas.items():

        for location1 in locations:
            for location2 in locations:

                if location1 != location2:

                    direction = (
                        location1[0] - location2[0],
                        location1[1] - location2[1],
                    )

                    for i in range(1, width):

                        antinode1 = (
                            location1[0] + i * direction[0],
                            location1[1] + i * direction[1],
                        )

                        if (
                            0 <= antinode1[0] <= height - 1
                            and 0 <= antinode1[1] <= width - 1
                        ):

                            print(location1, location2, antinode1)
                            antinodes.add(antinode1)
                        else:
                            break

                    for j in range(1, width):

                        antinode2 = (
                            location2[0] - j * direction[0],
                            location2[1] - j * direction[1],
                        )

                        if (
                            0 <= antinode2[0] <= height - 1
                            and 0 <= antinode2[1] <= width - 1
                        ):
                            print(location1, location2, antinode2)
                            antinodes.add(antinode2)
                        else:
                            break

                for location3 in locations:

                    if location3 != location1 and location3 != location2:


    #    print(antinodes)
    print(len(antinodes))


#        print(antenna_type, locations)


#        for char in line:
#            print(char)
# matrix = np.array([[char for char in line] for line in lines])
# print(matrix)


if __name__ == "__main__":
    main()
