#!/usr/bin/env python3
from collections import defaultdict
import math


def main():

    # read file
    f = open("day8.txt", "r")
    file_content = f.read()

    lines = file_content.split("\n\n")

    direction = lines[0]
    nodes = lines[1].split("\n")

    nodes_dict = {}

    for node_line in nodes:
        first_split = node_line.split("=")

        source_node = first_split[0].rstrip()
        dest_node_1 = first_split[1][2:5]
        dest_node_2 = first_split[1][7:10]

        nodes_dict[source_node] = (dest_node_1, dest_node_2)

    # part 1
    next_node = 'AAA'
    count_steps = 0
    i = 0

    while next_node != 'ZZZ':

        # check L or R command
        if direction[i] == 'L':
            next_node = nodes_dict[next_node][0]
        else:
            next_node = nodes_dict[next_node][1]

        # get next direction 
        i = (i + 1) % len(direction)
        count_steps += 1

    print(count_steps)

    ret = 1
    next_nodes = [node for node in nodes_dict.keys() if node[2] == 'A']
    for node in next_nodes:
        next_node = node
        count_steps = 0
        i = 0

        while next_node[2] != 'Z':

            # check L or R command
            if direction[i] == 'L':
                next_node = nodes_dict[next_node][0]
            else:
                next_node = nodes_dict[next_node][1]

            # get next direction 
            i = (i + 1) % len(direction)
            count_steps += 1

        ret = math.lcm(ret, count_steps)

    print(ret)

if __name__ == "__main__":
    main()
