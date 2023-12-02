import numpy as np

def read_input(filename):
    with open(filename) as file:
        line = file.readline().split(',')

    line = [int(num) for num in line] 
    return line

def simulate_fuel(positions):
    sorted_positions = sorted(positions)

    fuel = 0
    while (sorted_positions[0] != sorted_positions[len(sorted_positions)-1]):
        # find the crab that is the furthest of from the median
        median = np.median(sorted_positions)
        medians = [x - median for x in sorted_positions]
        furthest_idx = np.argmax(np.abs(medians))

        sorted_positions[furthest_idx] -= np.sign(medians[furthest_idx])
        fuel += 1

        #print(sorted_positions)

    return fuel

def simulate_fuel(positions):
    sorted_positions = sorted(positions)

    fuel = 0
    while (sorted_positions[0] != sorted_positions[len(sorted_positions)-1]):
        # find the crab that is the furthest of from the median
        median = np.median(sorted_positions)
        medians = [x - median for x in sorted_positions]
        furthest_idx = np.argmax(np.abs(medians))

        sorted_positions[furthest_idx] -= np.sign(medians[furthest_idx])
        fuel += 1

        #print(sorted_positions)

    return fuel


def calculate_fuel_median(positions):
    median = np.median(positions)
    fuel_cost = [np.abs(x - median) for x in positions]
    return np.sum(fuel_cost)

def calculate_fuel_mean(positions):
    mean = np.mean(positions)
    print(mean, round(mean))
    mean = int(mean)
    fuel_cost = [int(np.abs(x - mean)) for x in positions]
    #print(fuel_cost)
    fuel_cost = [sum([i for i in range(1, x+1)]) for x in fuel_cost]
    #print(fuel_cost)
    return np.sum(fuel_cost)

def main():
    positions = read_input("inputs/day7.txt")
    #positions = [16,1,2,0,4,2,7,1,2,14]
    #fuel_cost = simulate_fuel(positions)
    #print(fuel_cost)
    print(calculate_fuel_median(positions))
    print(calculate_fuel_mean(positions))

if __name__ == "__main__":
    main()