#!/usr/bin/env python3
import numpy as np


def read_map(lines):

    map = {}

    for line in lines:
        for i in range(len(line) - 1):
            start = line[i]
            end = line[i+1]
            direction = (end - start) / np.linalg.norm(end - start)

            while start[0] != end[0] or start[1] != end[1]:
                map[(int(start[0]), int(start[1]))] = '#'
                start += direction
            
            map[(int(start[0]), int(start[1]))] = '#'

    return map

def simulate_sandfall(abyss, map):

    first_down_the_abyss = False

    while True:
        sand_position = np.array((500, 0))

        while True:
            # break if sand falls down abyss
            if sand_position[1] == abyss + 1:

                # print the number of sand bits the first time one falls down the abyss
                if not first_down_the_abyss:
                    print(sum(type == 'o' for type in map.values()))
                    first_down_the_abyss = True
            
                map[(sand_position[0], sand_position[1])] = 'o'
                break

            # if sand is blocked...
            if (sand_position[0], sand_position[1]+1) in map:
                # try down left
                if (sand_position[0] - 1, sand_position[1] + 1) not in map:
                    sand_position[0] -= 1
                    sand_position[1] += 1
                # try down right
                elif (sand_position[0] + 1, sand_position[1] + 1) not in map:
                    sand_position[0] += 1
                    sand_position[1] += 1
                # stop
                else:
                    #print("\n")
                    map[(sand_position[0], sand_position[1])] = 'o'
                    break
            else:
                sand_position[1] += 1

        if (sand_position[0], sand_position[1]) == (500, 0):
            break 
    
    print(sum(type == 'o' for type in map.values()))


def main():

    f = open("inputs/day14.txt", "r").read()
    lines = [[np.array((float(coordinate.split(",")[0]), float(coordinate.split(
        ",")[1]))) for coordinate in lines.split("->")] for lines in f.split("\n")]
    #print(lines)

    depths = [x[1] for line in lines for x in line]
    abyss = max(depths) 

    map = read_map(lines)
    simulate_sandfall(abyss, map)




if __name__ == "__main__":
    main()
