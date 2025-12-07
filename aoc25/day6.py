#!/usr/bin/env python3
from collections import defaultdict
import numpy as np


def main():

    # read file
    lines = open("day6.txt", "r").read().split("\n")[:-1]

    worksheet = [[] for _ in range(len(lines[0].split()))]
    for line in lines:
        for i, num in enumerate(line.split()):
            worksheet[i].append(num)

    sum = 0
    for problem in worksheet:

        if problem[-1] == "+":
            result = np.sum(np.array(problem[:-1]).astype(int))
        if problem[-1] == "*":
            result = np.prod(np.array(problem[:-1]).astype(int))

        sum += result

    print(sum)


if __name__ == "__main__":
    main()
