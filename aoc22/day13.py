#!/usr/bin/env python3
import json
import itertools
from functools import cmp_to_key

def compare(left, right):

    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            return 1
        elif left == right:
            return 0
        else:
            return -1

    if left is None:
        return 1

    if right is None:
        return -1

    if isinstance(left, list) and isinstance(right, list):

        item_comparison = 0
        for item_left, item_right in itertools.zip_longest(left, right):

            item_comparison = compare(item_left, item_right)

            if item_comparison != 0:
                break
        
        return item_comparison

    if isinstance(left, list) and isinstance(right, int):
        return compare(left, [right])
    
    if isinstance(left, int) and isinstance(right, list):
        return compare([left], right)

def main():
    
    f = open("inputs/day13.txt", "r").read()
    pairs_raw = f.split("\n\n")

    # use json.loads to parse list from string directly
    pairs = [[json.loads(pair) for pair in pair_raw.split("\n")] for pair_raw in pairs_raw]

    indexes = [index+1 for index in range(len(pairs)) if compare(pairs[index][0], pairs[index][1]) == 1]
    print(sum(indexes))

    all_pairs = [json.loads(packet) for packet in f.split("\n") if packet != '']
    all_pairs.append([[2]])
    all_pairs.append([[6]])
    sorted_pairs = list(reversed(sorted(all_pairs, key=cmp_to_key(compare))))

    divider_2_index = sorted_pairs.index([[2]]) + 1
    divider_6_index = sorted_pairs.index([[6]]) + 1
    print(divider_2_index * divider_6_index)

if __name__ == "__main__":
    main()