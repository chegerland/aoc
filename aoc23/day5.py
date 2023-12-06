#!/usr/bin/env python3
from collections import defaultdict


def main():

    # read file
    f = open("day5_test.txt", "r")
    file_content = f.read()

    input = file_content.split("\n\n")

    seeds = []
    maps = []

    # read the input data
    for i, line in enumerate(input):

        # special case seeds
        if i == 0: 
            seeds = [int(seed) for seed in line.split(":")[-1].split()]
        else:

            # for every x-to-y map read in data as arrays
            first_split = line.split("\n")
            maps.append([])
            for j in range(1, len(first_split)):
                nums = [int(num) for num in first_split[j].split()]
                maps[i-1].append(nums)


    # part 1
    location = []
    for seed in seeds:

        current_num = seed        
        for map in maps:
            for mapping in map:
                if mapping[1] <= current_num <= mapping[1]+mapping[2]:
                    current_num = current_num - mapping[1] + mapping[0]
                    break


        location.append(current_num)

    print(min(location))


    # part 2 

    # read out intervals
    seed_ranges = []
    for i in range(0, len(seeds), 2):
        seed_ranges.append((seeds[i], seeds[i] + seeds[i+1]))


    # generate source intervals

    # for every source interval
    #   for every map type
    #       for every mapping
    #           map source interval to an array of output intervals

    for seed_interval in seed_ranges:

        current_intervals = [seed_interval]
        for map in maps:
            for mapping in map:
                # generate output intervals

def apply_map(source_intervals, map):

    output_intervals = []
    for interval in source_intervals:
        for mapping in map:
            # if no intersection, then values are the same
            if interval[1] <= mapping[1] or mapping[1]+mapping[2] <= interval[0]:
                continue
            else:
                overlap = (max(interval[0], mapping[1]), min(interval[1], mapping[1]+mapping[2]))
                print(f"Overlap: {overlap}")



#    print(seed_ranges)

    seed_ranges = [(47, 54)]
    for seed_range in seed_ranges:

        current_ranges = [seed_range]        
        ranges = []
#        for map in maps[0]:
        map = maps[0]
        for mapping in map:
            print(mapping)
            for current_range in current_ranges:
                # if no intersection, then values are the same
                if current_range[1] <= mapping[1] or mapping[1]+mapping[2] <= current_range[0]:
                    continue
                else:

                    # get part of source that lies in mapping

                    overlap = (max(current_range[0], mapping[1]), min(current_range[1], mapping[1]+mapping[2]))
                    print(f"Overlap: {overlap}")


        print(seed_range, ranges)







#    location = []
#    for seed in seeds:
#
#        current_num = seed        
#        for map in maps:
#            for mapping in map:
#                if mapping[1] <= current_num <= mapping[1]+mapping[2]:
#                    current_num = current_num - mapping[1] + mapping[0]
#                    break
#
#
#        location.append(current_num)
#
#    print(min(location))


#    print(seeds)
#    print(maps)
#    print(input)


if __name__ == "__main__":
    main()
