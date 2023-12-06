#!/usr/bin/env python3
from collections import defaultdict


def main():

    # read file
    f = open("day6.txt", "r")
    file_content = f.read()

    lines = file_content.split("\n")

    times = [int(time) for time in lines[0].split(":")[-1].split()]
    distances = [int(distance) for distance in lines[1].split(":")[-1].split()]

    # part 1
    score = 1
    for i, total_time in enumerate(times):

        ways_won = 0
        for time_held in range(0, total_time):
            distance = (total_time - time_held) * time_held

            if distance > distances[i]:
                ways_won += 1

        score *= ways_won

    print(score)

    total_time = int(''.join(lines[0].split(":")[-1].split()))
    record_distance = int(''.join(lines[1].split(":")[-1].split()))

    ways_won = 0
    for time_held in range(0, total_time):
        distance = (total_time - time_held) * time_held

        if distance > record_distance:
            ways_won += 1

    print(ways_won)


if __name__ == "__main__":
    main()
