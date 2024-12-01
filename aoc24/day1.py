#!/usr/bin/env python3
from collections import Counter

def main():

    # read file
    f = open("day1.txt", "r")
    #f = open("day1_test.txt", "r")

    file_content = f.read()
    
    lines = file_content.split("\n")

    list1 = []
    list2 = []

    # part 1 
    for line in lines:
        if line:
            first, second = line.split()

            list1.append(int(first))
            list2.append(int(second))

    list1.sort()
    list2.sort()

    total = 0
    for id1, id2 in zip(list1, list2):
        total += abs(id2 - id1)

    print(total)

    # part 2

    counter = Counter(list2)

    total2 = 0

    for id in list1:
        total2 += id * counter[id]
    print(total2)

if __name__ == "__main__":
    main()
