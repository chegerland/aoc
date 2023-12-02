#!/usr/bin/env python3
import string

def main():

    priority_encoding = dict()
    for index, letter in enumerate(string.ascii_lowercase):
       priority_encoding[letter] = index + 1
    for index, letter in enumerate(string.ascii_uppercase):
       priority_encoding[letter] = index + 27

    # read file
    f = open("inputs/day3.txt", "r")
    rucksacks = f.read().split("\n")

    priority_1 = 0
    for rucksack in rucksacks:
        length = len(rucksack)
        compartment_1 = rucksack[0:length//2]
        compartment_2 = rucksack[length//2:]

        # find common letters
        common_letters = set(compartment_1).intersection(set(compartment_2)) 

        for letter in common_letters:
            priority_1 += priority_encoding[letter]

    print(priority_1)

    priority_2 = 0
    for i in range(0,len(rucksacks),3):
        common_letters = set(rucksacks[i]).intersection(set(rucksacks[i+1])).intersection(set(rucksacks[i+2]))
        for letter in common_letters:
            priority_2 += priority_encoding[letter]
    
    print(priority_2)
    

if __name__ == "__main__":
    main()