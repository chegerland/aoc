#!/usr/bin/env python3

from collections import defaultdict
import queue

directions = [
    (0, 1),
    (1, 0),
    (0, -1),
    (-1, 0),
]

directions2 = [
    (0, 1),
    (1, 1),
    (1, 0),
    (1, -1),
    (0, -1),
    (-1, -1),
    (-1, 0),
    (-1, 1),
]


def main():

    # read file
    f = open("day12_test.txt", "r")

    lines = f.read().splitlines()

    plants = {}
    for i, line in enumerate(lines):
        for j, plant in enumerate(line):
            plants[(i, j)] = plant

    def find_neighbours(position):

        neighbours = []
        for direction in directions:
            if (
                position[0] + direction[0],
                position[1] + direction[1],
            ) in plants and plants[
                (position[0] + direction[0], position[1] + direction[1])
            ] == plants[
                position
            ]:
                neighbours.append(
                    (position[0] + direction[0], position[1] + direction[1])
                )

        return neighbours

    def get_verteces(position):

        verteces = {
            (1, 1): True,
            (1, -1): True,
            (-1, 1): True,
            (-1, -1): True,
        }

        for direction in directions2:
            if (
                position[0] + direction[0],
                position[1] + direction[1],
            ) in plants and plants[
                (position[0] + direction[0], position[1] + direction[1])
            ] == plants[
                position
            ]:
                for vertex in verteces:
                    if vertex == direction:
                        verteces[direction] = not verteces[direction]
                        break
                    elif vertex[0] == direction[0] or vertex[1] == direction[1]:
                        verteces[vertex] = not verteces[vertex]

                print(position, direction, verteces)

        return 4 - sum(verteces.values())
        # return neighbours

    not_visited = list(plants.keys())

    def find_region(start_position):
        current_region = []
        current_region.append(start_position)
        area = 0
        circum = 0
        verteces = 0

        while current_region:

            position = current_region.pop()
            not_visited.remove(position)

            area += 1
            circum += 4
            verteces += 4

            neighbours = find_neighbours(position)

            for neighbour in neighbours:
                circum -= 1
                if neighbour in not_visited and neighbour not in current_region:
                    current_region.append(neighbour)

            print(position, area, circum, get_verteces(position))

        return area, circum, verteces

    total = 0
    while not_visited:
        start_pos = not_visited[0]
        area, circum, verteces = find_region(start_pos)
        print(area, circum, verteces, plants[start_pos])
        total += area * circum

    print(total)


if __name__ == "__main__":
    main()
