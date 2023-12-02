def read_input(filename):
    commands = []
    with open(filename) as file:
        for line in file:
            command = line.split()
            commands.append([command[0], int(command[1])])
    
    return commands

def first_task(commands):
    depth = 0
    horizontal_position = 0

    for command, value in commands:
        if command == "forward":
            horizontal_position += value
        elif command == "down":
            depth += value
        elif command == "up":
            depth -= value

    # 952, 1931, 1840243
    print(f"Depth: {depth}, Horizontal position: {horizontal_position}, Product: {depth * horizontal_position}")


def second_task(commands):
    aim = 0
    depth = 0
    horizontal_position = 0

    for command, value in commands:
        if command == "forward":
            horizontal_position += value
            depth += aim * value
        elif command == "down":
            aim += value
        elif command == "up":
            aim -= value

    # 894762, 1931, 1727785422
    print(f"Depth: {depth}, Horizontal position: {horizontal_position}, Product: {depth * horizontal_position}")

def main():

    commands = read_input("inputs/day2.txt")

    first_task(commands)
    second_task(commands)


if __name__ == "__main__":
    main()