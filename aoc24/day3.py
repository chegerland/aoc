#!/usr/bin/env python3
import re

def main():

    # read file
    f = open("day3.txt", "r")
    string = f.read()

    # part 1
    matches = re.findall("mul\(\d+,\d+\)", string)

    total = 0
    for match in matches: 
        a, b = match[4:-1].split(",")

        total += int(a) * int(b)

    print(total)

    # part 2
    matches = re.findall("(mul\(\d+,\d+\))|(do\(\))|(don't\(\))", string)
    matches = [tuple(j for j in i if j)[-1] for i in matches]

    total = 0
    enabled = True
    for match in matches:


        if match == 'do()':
            enabled = True
        
        if match == "don't()":
            enabled = False
        
        if enabled and match[0:3] == 'mul':
            a, b = match[4:-1].split(",")
            total += int(a) * int(b)

    print(total)





if __name__ == "__main__":
    main()
