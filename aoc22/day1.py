#!/usr/bin/env python3

def main():

    # read file
    f = open("inputs/day1.txt", "r")
    file_content = f.read()
    
    elves = file_content.split("\n\n")

    # populate array with total calories per elve
    calories_per_elve = []
    for elve in elves:
        calories = [ int(calorie) for calorie in elve.split() ]
        calories_per_elve.append(sum(calories))

    # sort this array (from smallest to biggest)
    calories_per_elve.sort()
    
    # answer to part one
    print(calories_per_elve[-1])

    # answer to part two
    print(sum(calories_per_elve[-3:]))

if __name__ == "__main__":
    main()