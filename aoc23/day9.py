#!/usr/bin/env python3
import math


def main():

    # read file
    f = open("day9.txt", "r")
    file_content = f.read()

    lines = file_content.split("\n")

    right_sum = 0
    left_sum = 0
    for line in lines:

        time_series = [int(num) for num in line.split()]

        arrays = [time_series]
        step = 0
        right_value = time_series[-1]

        while not all(num == 0 for num in arrays[step]):
            new_array = [arrays[step][i+1] - arrays[step][i]
                         for i in range(len(arrays[step])-1)]

            arrays.append(new_array)

            step += 1
            right_value += new_array[-1]

        right_sum += right_value

        left_value = 0
        for array in reversed(arrays):
            left_value = array[0] - left_value

        left_sum += left_value

        # print(right_sum)
    print(left_sum)


if __name__ == "__main__":
    main()
