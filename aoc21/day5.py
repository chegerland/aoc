import numpy as np

def read_input(filename):
    lines = []
    with open(filename) as file:
        for line in file:
            split_line = line.split()
            (x0, y0) = split_line[0].split(',')
            (x1, y1) = split_line[2].split(',')
            lines.append([int(x0), int(y0), int(x1), int(y1)])
    return lines

def get_straight_lines(lines):
    straight_lines = []
    for line in lines:
        if line[0] == line[2] or line[1] == line[3]:
            straight_lines.append(line) 
    
    return straight_lines

def calculate_points(straight_lines):
    vents = {}
    for line in straight_lines:
        if line[0] == line[2]:
            points = sorted([line[1], line[3]])
            for i in range(points[0], points[1] + 1):
                if (line[0], i) not in vents:
                    vents[(line[0], i)] = 1
                else:
                    vents[(line[0], i)] += 1
        elif line[1] == line[3]:
            points = sorted([line[0], line[2]])
            for i in range(points[0], points[1] + 1):
                if (i, line[1]) not in vents:
                    vents[(i, line[1])] = 1
                else:
                    vents[(i, line[1])] += 1
        else:
            print("DIAGONAL LINE DETECTED")
            break
    return vents

def calculate_points_diag(lines):
    vents = {}
    for line in lines:
        if line[0] == line[2]:
            points = sorted([line[1], line[3]])
            for i in range(points[0], points[1] + 1):
                if (line[0], i) not in vents:
                    vents[(line[0], i)] = 1
                else:
                    vents[(line[0], i)] += 1
        elif line[1] == line[3]:
            points = sorted([line[0], line[2]])
            for i in range(points[0], points[1] + 1):
                if (i, line[1]) not in vents:
                    vents[(i, line[1])] = 1
                else:
                    vents[(i, line[1])] += 1
        else:
            # get x direction_x
            direction_x = 0
            if line[2] >= line[0]:
                direction_x = 1
            else:
                direction_x = -1
            
            direction_y = 0
            if line[3] >= line[1]:
                direction_y = 1
            else:
                direction_y = -1

            point = (line[0], line[1])
            while point != (line[2], line[3]):
                if point not in vents:
                    vents[point] = 1
                else:
                    vents[point] += 1

                point_l = list(point)
                point = (point_l[0] + direction_x, point_l[1] + direction_y)

            point = (line[2], line[3]) 
            if point not in vents:
                vents[point] = 1
            else:
                vents[point] += 1
            

    return vents

def main():

    lines = read_input("inputs/day5.txt")
    straight_lines = get_straight_lines(lines)
    vents = calculate_points(straight_lines)
    count = sum(value >= 2 for value in vents.values())
    print(count)

    vents = calculate_points_diag(lines)
    count = sum(value >= 2 for value in vents.values())
    print(count)

if __name__ == "__main__":
    main()