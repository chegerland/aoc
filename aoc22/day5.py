#!/usr/bin/env python3
from copy import deepcopy


def parse_stacks(stacks_raw):
    stack_rows = [list(rows) for rows in stacks_raw.split("\n")]

    index = 1
    stacks = []
    while str(index) in stack_rows[-1]:

        # create a new stack
        new_stack = []

        # find column index
        stack_index = stack_rows[-1].index(str(index))

        # reverse iterate through the rows, adding crates to the stack
        for i in range(len(stack_rows)-2, -1, -1):
            crate = stack_rows[i][stack_index]
            if crate != " ":
                new_stack.append(crate)

        stacks.append(new_stack)

        index += 1

    return stacks


def parse_instructions(instructions_raw):
    instructions = []

    for instruction in instructions_raw.split("\n"):
        words = instruction.split(" ")
        instructions.append([int(words[1]), int(words[3]), int(words[5])])

    return instructions


def use_crate_mover_9000(instruction, stacks):
    amount = instruction[0]
    source = stacks[instruction[1]-1]
    target = stacks[instruction[2]-1]

    # remove items from source and add to target
    for i in range(amount):
        crate = source.pop()
        target.append(crate)


def use_crate_mover_9001(instruction, stacks):
    amount = instruction[0]
    source = stacks[instruction[1]-1]
    target = stacks[instruction[2]-1]

    # remove items from source
    crates = []
    for i in range(amount):
        crates.append(source.pop())

    # attach reversed list of crates to target
    target.extend(list(reversed(crates)))


def main():

    # read file
    f = open("inputs/day5.txt", "r")
    stacks_raw, instructions_raw = f.read().split("\n\n")

    stacks = parse_stacks(stacks_raw)
    # need deep copy because the perform instructions in place (deep copy = copy of each interior object)
    stacks_2 = deepcopy(stacks)
    instructions = parse_instructions(instructions_raw)

    for instruction in instructions:
        use_crate_mover_9000(instruction, stacks)
        use_crate_mover_9001(instruction, stacks_2)

    answer_string_1 = [stack.pop() for stack in stacks]
    answer_string_2 = [stack.pop() for stack in stacks_2]

    print("".join(answer_string_1))
    print("".join(answer_string_2))


if __name__ == "__main__":
    main()
