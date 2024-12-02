#!/usr/bin/env python3

def check_list(levels):
    ascending = levels[0] < levels[1]
    
    is_safe = True
    for i in range(1, len(levels)):
    
        # ordering not ok
        if (levels[i - 1] < levels[i]) != ascending:
            is_safe = False
            break
    
        if not 1 <= abs(levels[i - 1] - levels[i]) <= 3:
            is_safe = False
            break

    return is_safe

def main():

    # read file
    #f = open("day2_test.txt", "r")
    f = open("day2.txt", "r")

    file_content = f.read()
    
    lines = file_content.split("\n")
    lines = lines[:-1]

    # part 1 
    total_safes = 0
    for line in lines:
        levels = list(map(int, line.split()))

        if check_list(levels):
            total_safes += 1
    
    print(total_safes)  

    # part 2 
    total_safes = 0
    for line in lines:
        levels = list(map(int, line.split()))

        if check_list(levels):
            total_safes += 1
        else:
            for i in range(len(levels)):
                if check_list(levels[0:i] + levels[i+1:]):
                    total_safes += 1
                    break

    print(total_safes)  
        





if __name__ == "__main__":
    main()
