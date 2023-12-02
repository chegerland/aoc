import numpy as np

def read_input(filename):
    inputs = []
    outputs = []
    with open(filename) as file:
        for line in file:
            IO = line.split('|')
            inputs.append([frozenset(list(char)) for char in IO[0].split()])
            outputs.append([frozenset(list(char)) for char in IO[1].split()])
    
    return inputs, outputs

def count_easy_digits(outputs):
    uniques = [2, 3, 4, 7]
    count = 0
    for line in outputs:
        for entry in line:
            if len(entry) in uniques:
                count +=1
    return count

def get_decoder(line):

    # sort strings according to length [1,7,4,(2,3,5),(0,6,9),8]
    sorted_line = sorted(line, key=len)
    
    num2code = {}

    # set the easy digits
    num2code[1] = sorted_line[0]
    num2code[7] = sorted_line[1]
    num2code[4] = sorted_line[2]
    num2code[8] = sorted_line[9]

    len5_digits = sorted_line[3:6]
    for entry in len5_digits:
        # 3 contains 1 fully
        if num2code[1] <= entry:
            num2code[3] = entry
        # 5 contains 4 - 1
        elif num2code[4].difference(num2code[1]) <= entry:
            num2code[5] = entry
        else:
            num2code[2] = entry
    
    len6_digits = sorted_line[6:9]
    for entry in len6_digits:
        if not num2code[1] <= entry:
            num2code[6] = entry
        elif num2code[4] <= entry:
            num2code[9] = entry
        else:
            num2code[0] = entry

    code2num = {k: v for v, k in num2code.items()}

    return code2num

def decode_output(inputs, outputs):

    total_sum = 0

    for input, output in zip(inputs, outputs):
        decoder = get_decoder(input)

        digit_list = []
        for entry in output:
            number = decoder[entry]
            digit_list.append(str(number))

        number = int(''.join(map(str,digit_list)))

        total_sum += number

        #print(number)

    return total_sum


    
def main():
    inputs, outputs = read_input("inputs/day8.txt")
    #inputs, outputs = read_input("inputs/test_input_8.txt")
    #count = count_easy_digits(outputs)
    #print(count)

    print(decode_output(inputs, outputs))

if __name__ == "__main__":
    main()