#!/usr/bin/env python3


def get_next_digit(bank, last_digit_position, digit_order):

    highest_digit = 0
    highest_digit_pos = -1
    for j in range(len(bank)):
        if len(bank) - j < 12 - digit_order:  # change 12 to 2 for part 1
            break
        if int(bank[j]) > highest_digit and j > last_digit_position:
            highest_digit = int(bank[j])
            highest_digit_pos = j

    return highest_digit, highest_digit_pos


def main():

    # read file
    lines = open("day3.txt", "r").read().split("\n")[:-1]

    total_joltage = 0
    for bank in lines:

        digit_pos = -1
        digits = []
        for i in range(12):  # change 12 to 2 for part 1
            new_highest_digit, digit_pos = get_next_digit(bank, digit_pos, i)
            digits.append(str(new_highest_digit))

        total_joltage += int("".join(digits))

    print(total_joltage)


if __name__ == "__main__":
    main()
