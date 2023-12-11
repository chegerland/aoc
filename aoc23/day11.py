#!/usr/bin/env python3
import numpy as np


def main():

    # read file
    array = np.loadtxt("day11.txt", dtype=str, comments=None)
    array = np.array([[0 if c == '.' else 1 for c in row] for row in array])

    empty_rows = np.where(~array.any(axis=1))[0]

    rows_added = 0
    for empty_row in empty_rows:
        array = np.insert(array, empty_row+rows_added, 0, axis=0)
        rows_added += 1

    empty_columns = np.where(~array.any(axis=0))[0]

    columns_added = 0
    for empty_column in empty_columns:
        array = np.insert(array, empty_column+columns_added, 0, axis=1)
        columns_added += 1

    galaxies = {}
    num_galaxy = 1
    for index, x in np.ndenumerate(array):

        if array[index] == 1:
            galaxies[index] = num_galaxy
            num_galaxy += 1

    distance_dict = {}
    for galaxy_pos, galaxy_num in galaxies.items():
        for galaxy2_pos, galaxy2_num in galaxies.items():

            if galaxy_pos == galaxy2_pos:
                continue

            distance_dict[frozenset([galaxy_num, galaxy2_num])] = abs(
                galaxy_pos[0] - galaxy2_pos[0]) + abs(galaxy_pos[1] - galaxy2_pos[1])

    sum = 0
    for pair, dist in distance_dict.items():
        sum += dist

    print(sum)


if __name__ == "__main__":
    main()
