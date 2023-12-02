import numpy as np


def read_input(filename):
    all_points = []
    fold_lines = []
    with open(filename) as file:
        for line in file:
            if line.startswith("fold"):
                split_line = line.split()
                split_again = split_line[2].split("=")
                fold_lines.append([split_again[0], int(split_again[1])])
            elif line == "\n":
                pass
            else:
                points = [int(num)
                          for num in list(line.split(",")) if num != "\n"]
                all_points.append((points[0], points[1]))

    return set(all_points), fold_lines


def make_fold(points, fold):
    new_points = set()
    if fold[0] == "x":
        fold_line_x = fold[1]

        for point in points:
            x, y = point
            if x <= fold_line_x:
                new_points.add(point)
            else:
                new_x = fold_line_x - (x - fold_line_x)
                new_points.add((new_x, y))
    else:
        fold_line_y = fold[1]

        for point in points:
            x, y = point
            if y <= fold_line_y:
                new_points.add(point)
            else:
                new_y = fold_line_y - (y - fold_line_y)
                new_points.add((x, new_y))

    return new_points


def make_all_folds(points, folds):
    old_points = points
    for fold in folds:
        new_points = make_fold(old_points, fold)
        old_points = new_points

    return old_points


def show_points(points):
    max_x = max([x for x, _ in points])
    max_y = max([y for _, y in points])
    print(max_x, max_y)

    array = np.full((max_x+1, max_y+1), '.')

    for point in points:
        array[point] = "#"

    print(array)


def main():
    #points, fold_lines = read_input("inputs/test_input_13.txt")
    points, fold_lines = read_input("inputs/day13.txt")

    new_points = make_fold(points, fold_lines[0])
    print(len(new_points))

    new_points = make_all_folds(points, fold_lines)
    print(new_points)

    show_points(new_points)


if __name__ == "__main__":
    main()
