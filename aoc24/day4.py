#!/usr/bin/env python3

from collections import defaultdict


def main():

    # read file
    f = open("day5.txt", "r")
    # f = open("day5_test.txt", "r")

    lines = f.read()

    orderings, strings = lines.split("\n\n")

    order_dict_less = defaultdict(list)
    for ordering in orderings.splitlines():

        first, second = ordering.split("|")
        order_dict_less[first].append(second)

    total = 0
    total2 = 0
    for string in strings.splitlines():
        numbers = string.split(",")

        is_correct = True
        for i, number in enumerate(numbers):
            for j, number2 in enumerate(numbers):

                if j < i:
                    if number2 in order_dict_less[number]:
                        is_correct = False
                        break

            if not is_correct:
                break

        if is_correct:
            total += int(numbers[int(len(numbers) / 2)])

        if not is_correct:

            for i in range(len(numbers) - 1):
                for j in range(len(numbers) - i - 1):
                    if numbers[j] in order_dict_less[numbers[j + 1]]:
                        numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

            total2 += int(numbers[int(len(numbers) / 2)])

    print(total)
    print(total2)


if __name__ == "__main__":
    main()
