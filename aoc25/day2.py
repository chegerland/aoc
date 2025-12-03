#!/usr/bin/env python3
from collections import Counter


def get_string_partition(string, num_parts):

    # string should be divisible by
    assert len(string) % num_parts == 0

    parts = []

    for i in range(int(len(string) / num_parts)):
        parts.append(string[i * num_parts : (i + 1) * num_parts])

    return parts


def parts_are_equal(array_of_parts):

    first_part = array_of_parts[0]
    are_same = True
    for i in range(1, len(array_of_parts)):
        if array_of_parts[i] != first_part:
            are_same = False
            break

    return are_same


def is_invalid(id):

    # odd length ids are always valid
    if len(id) % 2 == 1:
        return False

    # initial values
    id_parts = [id]
    len_of_parts = len(id)

    #    print(id, len_of_parts)

    is_invalid = False
    while True:

        # break if only single digits
        if len_of_parts <= 1:
            break

        # odd parts cant be halved --> break
        if len_of_parts % 2 == 1:
            break

        new_parts = []

        while id_parts:
            part = id_parts.pop()
            new_parts.append(part[: int(len(part) / 2)])
            new_parts.append(part[int(len(part) / 2) :])
            len_of_parts = int(len(part) / 2)

        # print(new_parts, len_of_parts)
        id_parts = new_parts

        if parts_are_equal(id_parts):
            is_invalid = True
            break

    return is_invalid


def main():

    # read file
    lines = open("day2.txt", "r").read().split("\n")[:-1]

    ranges = lines[0].split(",")

    sum_of_invalid_ids = 0

    for id_range in ranges:

        first_id, last_id = id_range.split("-")

        # part 1
        #        current_id = int(first_id)
        #        while current_id < int(last_id) + 1:
        #            if is_invalid(str(current_id)):
        #                sum_of_invalid_ids += current_id
        #                print(f"Invalid ID: {current_id}")
        #            current_id += 1

        # part 2
        current_id = first_id
        while int(current_id) < int(last_id) + 1:

            for i in range(1, len(current_id)):

                if len(current_id) % i == 0:
                    parts = get_string_partition(current_id, i)

                    if parts_are_equal(parts):
                        print(f"Invalid ID: {current_id}")
                        sum_of_invalid_ids += int(current_id)
                        break

            current_id = str(int(current_id) + 1)

    print(sum_of_invalid_ids)


#        print(first_id, is_invalid(first_id))


#    print(lines)


if __name__ == "__main__":
    main()
