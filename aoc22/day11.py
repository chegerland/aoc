#!/usr/bin/env python3
import operator

ops = {
    '*': operator.mul,
    '+': operator.add
}

class Monkey():
    def __init__(self, id, items, operation, divisible_by, throws_to) -> None:
        self.id = id
        self.items = items
        self.operation = operation
        self.divisible_by = divisible_by
        self.throws_to = throws_to

        self.inspected_items = 0

    def __repr__(self) -> str:
        return str(self.items)

def get_puzzle_answer(monkeys):
    inspected_items = [monkey.inspected_items for monkey in monkeys]
    inspected_items.sort()
    print(inspected_items[-2] * inspected_items[-1])

def do_monkey_business(monkeys, modulo, do_task_one):
    for monkey in monkeys:
            # for every item ...
        while monkey.items:
            item = monkey.items.pop(0)
            monkey.inspected_items += 1

                # do worry level calculation
            if monkey.operation[1] == 'old':
                worry_level = ops[monkey.operation[0]](item, item)
            else:
                worry_level = ops[monkey.operation[0]](item, int(monkey.operation[1]))

                # divide by 3
#                worry_level -= (worry_level // (3 * monkey.divisible_by)) * 3 * monkey.divisible_by
            if do_task_one:
                worry_level = worry_level // 3
            else:
                worry_level = worry_level % modulo

                # check condition
            if worry_level % monkey.divisible_by == 0:
                monkeys[monkey.throws_to[0]].items.append(worry_level)
            else:
                monkeys[monkey.throws_to[1]].items.append(worry_level)

def init_monkeys(monkeys_raw):
    monkeys = []

    for monkey in monkeys_raw:
        lines = monkey.split("\n")

        id = int(lines[0][-2])
        items = [int(item) for item in lines[1].split("Starting items:")[1].split(",")]
        operation = (lines[2].split(" ")[-2], lines[2].split(" ")[-1])
        divisible_by = int(lines[3].split(" ")[-1])
        throws_to = (int(lines[4].split(" ")[-1]), int(lines[5].split(" ")[-1]))

        monkeys.append(Monkey(id, items, operation, divisible_by, throws_to))
    return monkeys

def main():

    f = open("inputs/day11.txt", "r")
    monkeys_raw = f.read().split("\n\n")

    monkeys = init_monkeys(monkeys_raw)

    modulo = 3
    for monkey in monkeys:
        modulo *= monkey.divisible_by

    for _ in range(20):
        do_monkey_business(monkeys, modulo, True)
    
    get_puzzle_answer(monkeys)

    monkeys = init_monkeys(monkeys_raw)
    for _ in range(10000):
        do_monkey_business(monkeys, modulo, False)
    
    get_puzzle_answer(monkeys)


if __name__ == "__main__":
    main()
