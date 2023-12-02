import numpy as np
from collections import defaultdict, Counter
import pprint


def read_input(filename):
    graph = defaultdict(set)
    with open(filename) as file:
        for line in file:
            characters = line.split("-")
            start = characters[0]
            end = characters[1].rstrip('\n')

            graph[start].add(end)
            graph[end].add(start)

    return graph


def get_all_paths(graph, current_cave, all_paths, current_path):

    if current_cave != "end":
        # get the next possible caves
        connected_caves = graph[current_cave]
        next_possible_caves = []
        for next_cave in connected_caves:
            if next_cave.isupper():
                next_possible_caves.append(next_cave)
            else:
                if next_cave not in current_path:
                    next_possible_caves.append(next_cave)

        # create new path for each of them
        for next_cave in next_possible_caves:
            new_path = current_path.copy()
            new_path.append(next_cave)
            all_paths.append(new_path)
            get_all_paths(graph, next_cave, all_paths, new_path)


def get_all_paths_2(graph, current_cave, all_paths, current_path):

    if current_cave != "end":
        # get the next possible caves
        connected_caves = graph[current_cave]
        next_possible_caves = []
        for next_cave in connected_caves:
            # if its a big cave no problem
            if next_cave.isupper():
                next_possible_caves.append(next_cave)
            else:
                # get counts for all lower case caves
                cave_count = [count == 2 for key, count in Counter(
                    current_path).items() if key.islower()]

                if next_cave == "start":
                    pass
                elif next_cave == "end":
                    if Counter(current_path)[next_cave] == 0:
                        next_possible_caves.append(next_cave)
                    else:
                        pass
                else:
                    if any(cave_count) and Counter(current_path)[next_cave] >= 1:
                        pass
                    else:
                        next_possible_caves.append(next_cave)

                # create new path for each of them
        for next_cave in next_possible_caves:
            new_path = current_path.copy()
            new_path.append(next_cave)
            all_paths.append(new_path)
            get_all_paths_2(graph, next_cave, all_paths, new_path)


def filter_paths(all_paths):
    paths = []
    for path in all_paths:
        if path[0] == "start" and path[-1] == "end":
            paths.append(path)
    return paths


def main():
    graph = read_input("inputs/day12.txt")
    #graph = read_input("inputs/test_input_12_3.txt")
    pretty_print = pprint.PrettyPrinter()

    all_paths = []
    # get_all_paths(graph, "start", all_paths, ["start"])
    # paths = filter_paths(all_paths)
    # pretty_print.pprint(paths)
    # print(len(paths))

    get_all_paths_2(graph, "start", all_paths, ["start"])
    paths = filter_paths(all_paths)
    # pretty_print.pprint(all_paths)
    print(len(paths))


if __name__ == "__main__":
    main()
