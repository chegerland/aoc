#!/usr/bin/env python3
import numpy as np

cycles = {
    'noop': 1,
    'addx': 2
}

crt = np.array([["."] * 40] * 6)

def print_crt():
    for line in crt:
        print("".join(line))
    print("\n")

def main():

    f = open("inputs/day10.txt", "r")
    instructions = [line for line in f.read().split("\n")]

    register = 1
    cycle = 1
    signal_strength = 0

    crt_x = 0
    crt_y = 0

    for instruction in instructions:
        operation = instruction.split(" ")[0]

        for _ in range(cycles[operation]):

            if crt_x in [register - 1, register, register + 1]:
                crt[crt_y][crt_x] = "#"

            # before cycle
            if cycle == 20:
                signal_strength += register * 20
            elif cycle % 40 == 20:
                signal_strength += register * cycle

            crt_x = cycle % 40
            crt_y = cycle // 40
            
            cycle += 1

        # end cycle
        if operation == 'addx':
            register += int(instruction.split(" ")[1])

    print(signal_strength)
    print_crt()



if __name__ == "__main__":
    main()
