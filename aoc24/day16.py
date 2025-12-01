#!/usr/bin/env python3

from collections import defaultdict
import queue
import numpy as np
from math import floor, ceil
import sys

directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]


def main():

    # read file
    f = open("day16_test.txt", "r")
    # f = open("day16.txt", "r")

    lines = f.read().splitlines()

    start = ()
    end = ()
    g_score = {}
    f_score = {}
    inf = 1e19

    for i, line in enumerate(lines):
        for j, char in enumerate(line):

            if char == "S":
                start = (i, j)
                g_score[start] = 0
                f_score[start] = 0
            elif char == "E":
                end = (i, j)
                g_score[end] = inf
                f_score[end] = inf
            elif char == ".":
                g_score[(i, j)] = inf
                f_score[(i, j)] = inf

    print(f_score)
    # do a star, just copy from https://www.redblobgames.com/pathfinding/a-star/implementation.html#python-astar

    def h(a, b):
        (x1, y1) = a
        (x2, y2) = b
        return abs(x1 - x2) + abs(y1 - y2)

    frontier = queue.PriorityQueue()
    frontier.put((0, (start, (0, 1))))
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0

    while not frontier.empty():

        prio, (current_pos, current_dir) = frontier.get()
        #    print(current_pos, current_dir, cost_so_far[current_pos])

        if current_pos == end:
            cost_so_far[end] = cost_so_far[came_from[current_pos]] + 1
            break

        neighbours = []
        for direction in directions:
            possible_neighbour = (
                current_pos[0] + direction[0],
                current_pos[1] + direction[1],
            )
            if possible_neighbour in f_score:
                neighbours.append((possible_neighbour, direction))

        for next, direction in neighbours:
            new_cost = cost_so_far[current_pos]

            # point in same or opposite direction
            if current_dir[0] == direction[0] or current_dir[1] == direction[1]:
                if current_dir == direction:
                    new_cost += 1
                else:
                    new_cost += 2001
            else:
                new_cost += 1001

            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                prio = new_cost + h(next, end)
                frontier.put((prio, (next, direction)))
                came_from[next] = current_pos

    # print(cost_so_far)
    print(cost_so_far[end])

    current = end
    path = []

    while current != start:
        path.append(current)
        current = came_from[current]

    print(len(path))


if __name__ == "__main__":
    main()
