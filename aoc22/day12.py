#!/usr/bin/env python3
import string
import numpy as np

def main():
    
    encoding = dict()
    for index, letter in enumerate(string.ascii_lowercase):
       encoding[letter] = index + 1
    encoding['S'] = 0
    encoding['E'] = 27

    f = open("inputs/day12.txt", "r").read()
    rows = f.split("\n")
    matrix = np.array([[encoding[char] for char in str(row)] for row in rows])

    start = (np.argwhere(matrix == 0)[0][0], np.argwhere(matrix == 0)[0][1])
    end = (np.argwhere(matrix == 27)[0][0], np.argwhere(matrix == 27)[0][1])

    start_points = [(x, y) for (x, y) in np.argwhere(matrix == 1)]
    start_points.append(start)

    steps = {}

    for start_point in start_points:
        steps[start_point] = breadth_first_search(matrix, start_point, end)

    print(steps[start])
    print(min(steps.values()))


def breadth_first_search(matrix, start, end):
    x_size, y_size = matrix.shape

    queue = []
    explored = set()
    explored.add(start)
    queue.append((start[0], start[1], 0))

    while queue:
        (x, y, steps) = queue.pop(0)

        if (x, y) == end:
            return steps

        # get next possible neighbours
        for (x_n, y_n) in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
            if (0 <= x_n <= x_size - 1) and (0 <= y_n <= y_size - 1) and matrix[(x_n, y_n)] <= matrix[(x,y)] + 1:
                if (x_n, y_n) not in explored:
                    explored.add((x_n, y_n))
                    queue.append((x_n, y_n, steps + 1))

    return np.Inf
    
if __name__ == "__main__":
    main()
