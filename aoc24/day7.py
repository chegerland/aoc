#!/usr/bin/env python3

import numpy as np
from collections import defaultdict


def main():

    # read file
    f = open("day7.txt", "r")
    # f = open("day7_test.txt", "r")

    lines = f.read().splitlines()

    total = 0
    for line in lines:

        goal, rest = line.split(": ")
        goal = int(goal)

        numbers = rest.split(" ")
        numbers = [int(num) for num in numbers]

        # print(goal, numbers)

        results = defaultdict(list)
        results[0] = [numbers[0]]

        for i, number in enumerate(numbers):

            if i > 0:
                for num in results[i - 1]:
                    results[i].append(num * number)
                    results[i].append(int(str(num) + str(number)))
                    results[i].append(num + number)

        # print(results)
        # print(results[len(numbers) - 1])
        if goal in results[len(numbers) - 1]:
            total += goal

    print(total)


if __name__ == "__main__":
    main()
