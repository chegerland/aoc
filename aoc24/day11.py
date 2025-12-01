#!/usr/bin/env python3
from functools import cache


@cache
def length(stone, blinks):

    if blinks == 0:
        return 1

    if stone == 0:
        return length(1, blinks - 1)
    elif len(str(stone)) % 2 == 0:
        return length(
            int(str(stone)[0 : int(len(str(stone)) / 2)]), blinks - 1
        ) + length(int(str(stone)[int(len(str(stone)) / 2) :]), blinks - 1)
    else:
        return length(stone * 2024, blinks - 1)


def main():

    # read file
    f = open("day11.txt", "r")
    old_stones = [int(s) for s in f.read().split()]

    total = 0
    for stone in old_stones:
        total += length(stone, 25)
    print(total)

    total = 0
    for stone in old_stones:
        total += length(stone, 75)
    print(total)


if __name__ == "__main__":
    main()
