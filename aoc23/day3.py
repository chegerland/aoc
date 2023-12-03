#!/usr/bin/env python3

def main():

    # read file
    f = open("day3.txt", "r")
    file_content = f.read()
    
    lines = file_content.split("\n")

    # lets first fill dictionaries of the positions of every number and symbol
    numbers = {}
    symbols = {}

    for i in range(0, len(lines)):

        line = lines[i]

        num_detected = False
        num = []

        # loop through line
        for j in range(0, len(line)):

            # find symbol
            if not line[j].isdigit() and not line[j] == '.':
                symbols[(i,j)] = line[j]

            # append to detected number
            if line[j].isdigit():
                num_detected = True
                num.append(line[j])

            # stop if number is finished
            if num_detected:
                if not line[j].isdigit():
                    number = int(''.join(num))
                    numbers[(i, j-len(str(number)))] = number
                    num_detected = False
                    num = []

        # extra check if number is at the end of the line        
        if num_detected:
            number = int(''.join(num))
            numbers[(i, j-len(str(number)))] = number

    # part 1

    # for every number...
    total = 0
    for num_pos, number in numbers.items():

        # generate possible positions for symbol
        y, x = num_pos
        len_number = len(str(number))
        possible_positions = []

        for i in range(x-1, x+len_number+1):
            for j in range(y-1, y+2):
                possible_positions.append((j, i))

        # check if there is a symbol nearby
        for pos in possible_positions:
            if pos in symbols:
                total += number
                break

    print(total)

    # part 2

    total = 0
    # for every symbol...
    for sym_pos, symbol in symbols.items():

        # skip if its not a star
        if not symbol == "*":
            continue

        num_found = 0
        gear_ratio = 1

        # check all numbers
        for num_pos, number in numbers.items():

            # generate possible positions for symbol
            y, x = num_pos
            len_number = len(str(number))
            possible_positions = []

            for i in range(x-1, x+len_number+1):
                for j in range(y-1, y+2):
                    possible_positions.append((j, i))

            # check if the symbol is in position
            if sym_pos in possible_positions:
                num_found += 1
                gear_ratio *= number
            
        # if exactly two numbers are found, its a gear
        if num_found == 2:
            total += gear_ratio 
        
    print(total)


if __name__ == "__main__":
    main()