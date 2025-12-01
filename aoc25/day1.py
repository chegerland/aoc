#!/usr/bin/env python3
from collections import Counter


def main():

    # read file
    lines = open("day1.txt", "r").read().split("\n")[:-1]

    dial = 50

    zero_count = 0
    zero_point_count = 0
    for line in lines:

        turns = int(line[1:])

        while turns > 0:
            if line[0] == "R":
                dial += 1
            else:
                dial -= 1

            turns -= 1

            if dial > 99:
                dial = 0
            if dial < 0:
                dial = 99

            if dial == 0:
                zero_point_count += 1
        if dial == 0:
            zero_count += 1

    print(zero_count)
    print(zero_point_count)


if __name__ == "__main__":
    main()
