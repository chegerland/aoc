#!/usr/bin/env python3
from collections import defaultdict
import numpy as np


def main():

    # read file
    lines = open("day7.txt", "r").read().split("\n")[:-1]

    tachyon_manifold = np.array([[char for char in line] for line in lines])
    start_tachyon = np.where(tachyon_manifold == "S")

    # part 1
    # tachyons = set()
    # tachyons.add((start_tachyon[0][0], start_tachyon[1][0]))

    # splits = 0
    # while True:

    #    if next(iter(tachyons))[0] == len(tachyon_manifold) - 1:
    #        break

    #    new_tachyons = set()
    #    for tachyon in tachyons:

    #        # test new position
    #        new_tachyon = (tachyon[0] + 1, tachyon[1])

    #        if tachyon_manifold[new_tachyon] == ".":
    #            new_tachyons.add(new_tachyon)
    #        if tachyon_manifold[new_tachyon] == "^":
    #            splits += 1
    #            left = (tachyon[0] + 1, tachyon[1] - 1)
    #            right = (tachyon[0] + 1, tachyon[1] + 1)
    #            new_tachyons.add(left)
    #            new_tachyons.add(right)

    #    tachyons = new_tachyons

    #    print(new_tachyons)

    # print(splits)

    # part 2
    tachyons = defaultdict(int)
    tachyons[((start_tachyon[0][0], start_tachyon[1][0]))] = 1

    while True:

        if next(iter(tachyons))[0] == len(tachyon_manifold) - 1:
            break

        new_tachyons = defaultdict(int)
        for tachyon in tachyons.keys():

            # test new position
            new_tachyon = (tachyon[0] + 1, tachyon[1])

            if tachyon_manifold[new_tachyon] == ".":
                new_tachyons[new_tachyon] += tachyons[tachyon]
            if tachyon_manifold[new_tachyon] == "^":
                left = (tachyon[0] + 1, tachyon[1] - 1)
                right = (tachyon[0] + 1, tachyon[1] + 1)
                new_tachyons[left] += tachyons[tachyon]
                new_tachyons[right] += tachyons[tachyon]

        tachyons = new_tachyons

    #    print(tachyons)
    print(sum(tachyons.values()))


if __name__ == "__main__":
    main()
