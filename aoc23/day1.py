#!/usr/bin/env python3

def main():

    # read file
    f = open("day1.txt", "r")
    file_content = f.read()
    
    lines = file_content.split("\n")


    # part 1 
    total = 0
    for line in lines:

        # get only digits from string
        num_line = [int(char) for char in line if char.isdigit()]

        # some lines don't contain digits
        if num_line:
            total += num_line[0]*10 + num_line[-1]

    print(total) 

    # part 2

    num_dict = {
        'one': 1, 
        'two': 2, 
        'three': 3, 
        'four': 4, 
        'five': 5, 
        'six': 6, 
        'seven': 7, 
        'eight': 8, 
        'nine': 9, 
        }

    total = 0
    for line in lines:

        num_line = []

        i = 0
        while i < len(line):
            skip = 0

            # if its a digit, append immediately
            if line[i].isdigit():
                num_line.append(int(line[i]))

            # look for number words, if found skip by its length
            for key, value in num_dict.items():
                if key in line[i:i+len(key)]:
                    num_line.append(int(value))
                    skip = len(key)-1

            i += max(1, skip)

        num = num_line[0]*10 + num_line[-1]
        total += num

    print(total) 


if __name__ == "__main__":
    main()