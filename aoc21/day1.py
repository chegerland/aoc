def read_input(filename):
    heights = []
    with open(filename) as file:
        for current_height in file:
            heights.append(int(current_height))
    
    return heights

def get_total_increases(heights):
    last_height = 100000
    total_increases = 0
    for current_height in heights: 
        if int(current_height) > last_height:
            total_increases += 1
            
        last_height = int(current_height)
    return total_increases

def get_total_increases_windows(heights):
    last_heigts_sum = 100000
    total_increases = 0
    for i in range(3, len(heights) + 1):
        current_heights_sum = sum(heights[i-3:i])

        if current_heights_sum > last_heigts_sum:
            total_increases += 1
        
        last_heigts_sum = current_heights_sum
    
    return total_increases


def main():
    # read input into list
    heights = read_input("inputs/day1.txt")

    # get number of single increases
    total_increases = get_total_increases(heights)
    print(f"Total increases: {total_increases}") # 1715

    # get sliding window increases
    total_increases_windows = get_total_increases_windows(heights)
    print(f"Total increases window: {total_increases_windows}") # 1739


if __name__ == "__main__":
    main()