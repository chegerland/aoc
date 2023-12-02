from collections import defaultdict
from queue import PriorityQueue
import numpy as np

def read_input(filename):
    square = []
    with open(filename) as file:
        for line in file:
            # read number line
            numbers = [np.inf] + [int(num)
                                   for num in list(line) if num != '\n'] + [np.inf]
            square.append(np.array(numbers))

    square.insert(0, [np.inf] * len(square[0]))
    square.append([np.inf] * len(square[0]))

    return np.array(square)

def find_shortest_path(square):
    start_position = (1,1)
    end_position = (len(square[0])-2, len(square)-2)

    node2risk = {}
    #for i in range(0, len(square[0])):
    #    for j in range(0, len(square)):
    #        node2risk[(i, j)] = np.inf
    node2risk[(1,1)] = 0

    visited = set()

    queue = PriorityQueue()
    queue.put((0, start_position))

    while not queue.empty():

        # choose next queue item
        _, (i, j) = queue.get()
        risk = node2risk[(i, j)]

        # stop if end point is reached
        if (i, j) == end_position:
            break
        
        # mark this position as done
        visited.add((i, j))

        # get neighbour points
        neighbour_pos = [(i, j-1), (i, j+1), (i-1,j), (i+1, j)]

        for pos in neighbour_pos:
            # no walls, and no previously visited points
            if square[pos] == np.inf or pos in visited:
                continue
            
            # update risk
            new_risk = min(risk + square[pos], node2risk.get(pos, np.inf))
            node2risk[pos] = new_risk

            # method 1
            #score = new_risk
            #queue.put((score, pos))

            # method 2
            score = new_risk + np.sqrt((pos[0] - end_position[0])**2 + (pos[1] - end_position[1])**2)

            if pos in queue.queue:

            queue.put((score, pos))


    print(len(node2risk))
    return node2risk[end_position]

def main():
    square = read_input("inputs/test_input_15.txt")
    #print(square)
    print(find_shortest_path(square))


if __name__ == "__main__":
    main()