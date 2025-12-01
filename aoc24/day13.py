#!/usr/bin/env python3

from collections import defaultdict
import queue
import numpy as np


def main():

    # read file
    # f = open("day13_test.txt", "r")
    f = open("day13.txt", "r")

    machines = f.read().split("\n\n")

    total = 0
    for machine in machines:

        lines = machine.splitlines()

        button_a = np.array(
            [int(s.split("+")[-1]) for s in lines[0].split(":")[-1].split(",")]
        )
        button_b = np.array(
            [int(s.split("+")[-1]) for s in lines[1].split(":")[-1].split(",")]
        )
        prize = np.array(
            [int(s.split("=")[-1]) for s in lines[2].split(":")[-1].split(",")]
        )

        prize[0] += 10000000000000
        prize[1] += 10000000000000

        b = (button_a[0] * prize[1] - prize[0] * button_a[1]) / (
            button_a[0] * button_b[1] - button_a[1] * button_b[0]
        )
        a = (
            prize[0]
            - (button_a[0] * prize[1] - prize[0] * button_a[1])
            / (button_a[0] * button_b[1] - button_a[1] * button_b[0])
            * button_b[0]
        ) / button_a[0]

        if (abs(a - int(a)) < 1e-5) and (abs(b - int(b)) < 1e-5):
            total += 3 * a + b
            print(button_a, button_b, prize)

    print(total)


if __name__ == "__main__":
    main()
