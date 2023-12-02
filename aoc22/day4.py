#!/usr/bin/env python3
import string


def fully_contains(lower_1, upper_1, lower_2, upper_2):
    # 1 contains 2
    if lower_1 <= lower_2 and upper_1 >= upper_2:
        return True
    # 2 contains 1
    if lower_2 <= lower_1 and upper_2 >= upper_1:
        return True

    return False


def overlaps(lower_1, upper_1, lower_2, upper_2):
    # 1 overlaps with 2
    if lower_2 <= lower_1 <= upper_2 or lower_2 <= upper_1 <= upper_2:
        return True
    # 2 contains 1
    if lower_1 <= lower_2 <= upper_1 or lower_1 <= upper_2 <= upper_1:
        return True

    return False


def main():

    # read file
    f = open("inputs/day4.txt", "r")
    section_range_pairs = f.read().split("\n")

    count_full = 0
    count_overlap = 0
    for section_range_pair in section_range_pairs:
        section1, section2 = section_range_pair.split(",")
        lower_1, upper_1 = tuple(map(int, section1.split("-")))
        lower_2, upper_2 = tuple(map(int, section2.split("-")))

        if fully_contains(lower_1, upper_1, lower_2, upper_2):
            count_full += 1

        if overlaps(lower_1, upper_1, lower_2, upper_2):
            count_overlap += 1

    print(count_full)
    print(count_overlap)


if __name__ == "__main__":
    main()