#!/usr/bin/env python3
import numpy as np

encoding = {
    'L': np.array([-1,0]),
    'R': np.array([1,0]),
    'U': np.array([0,1]),
    'D': np.array([0,-1]),
}

def main():

    f = open("inputs/day9.txt", "r")
    instructions = [(instruction[0], int(instruction[2:])) for instruction in f.read().split("\n")]

    rope = [np.array([0, 0]) for _ in range(10)]

    visited_1 = set()
    visited_2 = set()

    for (direction, steps) in instructions:

        for _ in range(steps):
            rope[0] += encoding[direction]
            
            for id in range(1, len(rope)):
                if rope[id - 1][0] - 1 <= rope[id][0] <= rope[id - 1][0] + 1 and rope[id - 1][1] - 1 <= rope[id][1] <= rope[id - 1][1] + 1:
                    pass
                else: 
                    difference = rope[id - 1] - rope[id]
                    step_direction = np.array([x if abs(x) < 2 else np.sign(x) for x in difference])
                    rope[id] += step_direction

            visited_1.add((rope[1][0], rope[1][1]))
            visited_2.add((rope[9][0], rope[9][1]))

    print(len(visited_1)) 
    print(len(visited_2)) 


if __name__ == "__main__":
    main()
