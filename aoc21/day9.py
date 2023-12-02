import numpy as np

def read_input(filename):
    array = []
    with open(filename) as file:
        for line in file:
            # read number line
            numbers = [int(num) for num in list(line) if num != '\n']

            # pad with 9s
            numbers = [9] + numbers + [9]
            array.append(numbers)

        array.insert(0, [9] * len(array[0]))
        array.append([9] * len(array[0]))
    return np.array(array)

def check_tubes(array):

    sum_tubes = 0

    for i in range(1, len(array)-1):
        for j in range(1, len(array[0])-1):
            element = array[i][j]

            if element < array[i-1][j] and element < array[i+1][j] and element < array[i][j+1] and element < array[i][j-1]:
                sum_tubes += element + 1

    return sum_tubes

def get_low_point_positions(array):
    positions = []
    for i in range(1, len(array)-1):
        for j in range(1, len(array[0])-1):
            element = array[i][j]

            if element < array[i-1][j] and element < array[i+1][j] and element < array[i][j+1] and element < array[i][j-1]:
                positions.append((i,j))

    return positions

def get_basin_sizes(array):
    low_points = get_low_point_positions(array)

    basin_sizes = []
    
    for low_point in low_points:
        point_set = set()
        point_set.add(low_point)
        basin = get_basin(array, low_point, point_set)

        basin_sizes.append(len(basin))

    return basin_sizes

def puzzle_answer(basin_sizes):
    sorted_sizes = sorted(basin_sizes)
    return np.prod(sorted_sizes[-3:])
    

def get_basin(array, position, point_set):
    i, j = position
    element = array[i][j]

    # positions of all neighbours
    neighbours = [(i+1, j), (i-1,j), (i,j+1), (i,j-1)]

    # positions of all neighbours that are bigger than the current element
    bigger_neighbours = [(x, y) for (x, y) in neighbours if array[(x,y)] > element and array[(x,y)] != 9]

    # for all neighbours
    for neighbour_position in bigger_neighbours:
        point_set.add(neighbour_position)
        get_basin(array, neighbour_position, point_set)

    return point_set

def main():
    array = read_input("inputs/day9.txt")
    #array = read_input("inputs/test_input_9.txt")
    print(array)
    print(check_tubes(array))
    sizes = get_basin_sizes(array)
    print(puzzle_answer(sizes))

if __name__ == "__main__":
    main()