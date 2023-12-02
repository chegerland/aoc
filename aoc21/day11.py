import numpy as np


def read_input(filename):
    square = []
    with open(filename) as file:
        for line in file:
            # read number line
            numbers = [-np.inf] + [int(num)
                                   for num in list(line) if num != '\n'] + [-np.inf]
            square.append(np.array(numbers))

    square.insert(0, [-np.inf] * len(square[0]))
    square.append([-np.inf] * len(square[0]))

    return np.array(square)


def make_single_step(square, flashes):
    # increase energy level by one
    new_square = 1 + square

    # get all octopi that can flash
    index = np.where(new_square > 9)
    can_flash = [(i, j) for i, j in zip(index[0], index[1])]
    has_flashed = []

    while can_flash != []:

        # get the next point
        position = can_flash.pop()

        # flash the neighbours
        i, j = position
        neighbours = [(i, j+1), (i, j-1), (i+1, j+1), (i+1, j-1),
                      (i+1, j), (i-1, j+1), (i-1, j-1), (i-1, j)]

        for point in neighbours:
            new_square[point] += 1

            # if the neighbour hasnt_flashed yet, add it to the can_flash list
            if new_square[point] > 9 and point not in has_flashed and point not in can_flash:
                can_flash.append(point)

        # append this position to the has flashed list
        has_flashed.append(position)

    flashes += len(has_flashed)
    # set all octopi that flashed to zero
    new_square = np.where(new_square >= 10, 0, new_square)

    return new_square, flashes

    # print(mask)
    # print(new_square[mask])

    # print(square[square > 9])


def make_n_steps(square, n):

    flashes = 0
    old_square = square
    for i in range(0, n):
        new_square, flashes = make_single_step(old_square, flashes)
        old_square = new_square

    return old_square, flashes


def unpad_square(square):

    unpadded = np.delete(square, 0, axis=1)
    unpadded = np.delete(unpadded, -1, axis=1)
    unpadded = np.delete(unpadded, 0, axis=0)
    unpadded = np.delete(unpadded, -1, axis=0)
    return unpadded


def check_synchronization(square):

    old_square = square

    unpadded = unpad_square(square)
    flashes = 0
    step = 0
    while not np.all(unpad_square(old_square) == 0):
        new_square, flashes = make_single_step(old_square, flashes)
        old_square = new_square
        step += 1

    return step


def main():
    square = read_input("inputs/day11.txt")
    #square = read_input("inputs/test_input_11.txt")
    #print(make_n_steps(square, 1))
    #print(make_n_steps(square, 10))
    #print(make_n_steps(square, 195)[0])
    # print(unpad_square(square))
    print(check_synchronization(square))


if __name__ == "__main__":
    main()
