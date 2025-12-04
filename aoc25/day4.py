#!/usr/bin/env python3


def get_neighbour_position(pos):
    i, j = pos

    return [
        (i - 1, j - 1),
        (i - 1, j),
        (i - 1, j + 1),
        (i, j - 1),
        (i, j + 1),
        (i + 1, j - 1),
        (i + 1, j),
        (i + 1, j + 1),
    ]


def remove_rolls(roll_positions: set):

    if len(roll_positions) == 0:
        return 0

    new_roll_positions = roll_positions.copy()
    for roll_position in roll_positions:
        a, b = roll_position

        neighbours = get_neighbour_position((a, b))
        rolls = 0
        can_be_accessed = True
        for neighbour in neighbours:
            if rolls >= 4:
                break
            if neighbour in roll_positions:
                rolls += 1

        if rolls >= 4:
            can_be_accessed = False

        if can_be_accessed == True:
            new_roll_positions.remove((a, b))

    return new_roll_positions


def main():

    # read file
    lines = open("day4.txt", "r").read().split("\n")[:-1]

    roll_positions = set()
    for i, line in enumerate(lines):

        for j, element in enumerate(line):

            if element == "@":
                roll_positions.add((i, j))

    # part 1
    # access_count = 0
    # for roll_position in roll_positions:
    #    a, b = roll_position

    #    neighbours = get_neighbour_position((a, b))
    #    rolls = 0
    #    can_be_accessed = True
    #    for neighbour in neighbours:
    #        if rolls >= 4:
    #            break
    #        if neighbour in roll_positions:
    #            rolls += 1

    #    if rolls >= 4:
    #        can_be_accessed = False

    #    if can_be_accessed == True:
    #        access_count += 1

    #    print(len(roll_positions))

    # part 2
    new_roll_positions = remove_rolls(roll_positions)

    rolls_removed_total = 0
    while len(roll_positions) - len(new_roll_positions) > 0:

        rolls_removed = len(roll_positions) - len(new_roll_positions)
        # print(rolls_removed)
        rolls_removed_total += rolls_removed

        roll_positions = new_roll_positions
        new_roll_positions = remove_rolls(new_roll_positions)

    print(rolls_removed_total)


if __name__ == "__main__":
    main()
