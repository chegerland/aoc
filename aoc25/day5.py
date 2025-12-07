#!/usr/bin/env python3


def get_overlapping_ranges(id_ranges, next_id_range):

    overlapping_ranges = set()

    for id_range in id_ranges:

        overlap_range = range(int(id_range[0]), int(id_range[1]) + 1)

        if (
            int(next_id_range[0]) in overlap_range
            or int(next_id_range[1]) in overlap_range
        ):
            overlapping_ranges.add(id_range)

    return overlapping_ranges


def get_union_of_ids(overlapping_ranges, next_id_range):

    mins = []
    maxs = []

    for overlapping_range in overlapping_ranges:
        mins.append(overlapping_range[0])
        maxs.append(overlapping_range[1])

    return (min(mins + [next_id_range[0]]), max(maxs + [next_id_range[1]]))


def main():

    # read file
    fresh_id_ranges, available_ids = open("day5.txt", "r").read().split("\n\n")

    id_ranges = set()
    for fresh_id_range in fresh_id_ranges.split("\n"):
        start_id, end_id = fresh_id_range.split("-")
        id_ranges.add((start_id, end_id))

    # part 1

    #    how_many_fresh = 0
    #    for available_id in available_ids.split("\n")[:-1]:
    #
    #        for id_range in id_ranges:
    #
    #            if int(available_id) in range(int(id_range[0]), int(id_range[1]) + 1):
    #                #                print(available_id, "fresh")
    #                how_many_fresh += 1
    #                break
    #
    #    print(how_many_fresh)

    #    ranges_non_overlapping = set()

    non_overlapping_ids = set()

    while len(id_ranges) > 0:

        next_id_range = id_ranges.pop()

        # check if range has overlap with existing ones
        overlapping_ranges = get_overlapping_ranges(non_overlapping_ids, next_id_range)

        if len(overlapping_ranges) == 0:
            non_overlapping_ids.add(next_id_range)
        else:
            for overlapping_range in overlapping_ranges:
                non_overlapping_ids.remove(overlapping_range)
            union_of_ids = get_union_of_ids(overlapping_ranges, next_id_range)
            non_overlapping_ids.add(union_of_ids)

        print(next_id_range, non_overlapping_ids)

    sum = 0
    for non_overlapping_id_range in non_overlapping_ids:

        sum += int(non_overlapping_id_range[1]) + 1 - int(non_overlapping_id_range[0])

    print(sum)


#        print(id_ranges, next_id_range)
#
#        # see if its overlapping
#        overlap = False
#        for id_range in id_ranges:
#
#            overlap_range = range(int(id_range[0]), int(id_range[1]) + 1)
#
#            if (
#                int(next_id_range[0]) in overlap_range
#                or int(next_id_range[1]) in overlap_range
#            ):
#                print(f"Overlap: {next_id_range}, {id_range}")
#                overlap = True
#                #                overlapping_id_range = id_range
#
#        if overlap:
#            overlapping_range = id_ranges.remove(id_range)
#            print(id_ranges, id_range, overlapping_range)
#            non_overlapping_ids.add(
#                (
#                    min(next_id_range[0], overlapping_range[0]),
#                    max(next_id_range[1], overlapping_range[1]),
#                )
#            )
#        else:
#            non_overlapping_ids.add(next_id_range)
#
#    print(non_overlapping_ids)


#    non_overlapping
#
#    for id_range in id_ranges:
#
#        for i in range(0, int(len(id_ranges) / 2) + 1):
#
#            if id_range == id_ranges[i]:
#                continue
#
#            overlap_range = range(int(id_ranges[i][0]), int(id_ranges[i][1]) + 1)
#
#            if int(id_range[0]) in overlap_range or int(id_range[1]) in overlap_range:
#                print(f"Overlap: {id_range}, {id_ranges[i]}")


#        # check if range has overlap
#        overlap = False
#        for range_non_overlapping in ranges_non_overlapping:
#            overlap_range = range(
#                int(range_non_overlapping[0]), int(range_non_overlapping[1]) + 1
#            )
#
#            # if it has overlap...
#            if int(id_range[0]) in overlap_range or int(id_range[1]) in overlap_range:
#                # add the union to the set
#                overlap = True
#                break
#                print(id_range)
#
#        if overlap:
#            ranges_non_overlapping.remove(range_non_overlapping)
#            ranges_non_overlapping.add(
#                (
#                    min(id_range[0], range_non_overlapping[0]),
#                    max(id_range[1], range_non_overlapping[1]),
#                )
#            )
#
#        else:
#            # if not --> add it to ranges non overlapping
#            ranges_non_overlapping.add(id_range)

#    print(ranges_non_overlapping)


if __name__ == "__main__":
    main()
