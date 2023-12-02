def read_input(filename):
    report = []
    with open(filename) as file:
        for line in file:
            numbers = list(line.rstrip('\n'))
            report.append(numbers)
    
    return report

def count_bits(report):
    # create list that counts zeros and ones for each position
    counts = [0 for i in range(0, len(report[0]))]

    for numbers in report:
        for i in range(0, len(numbers)):
            if numbers[i] == '1':
                counts[i] += 1
            else:
                counts[i] -= 1

    return counts    

def get_rates(counts):
    gamma_rate = []
    epsilon_rate = []
    for entry in counts:
        if entry >= 0:
            gamma_rate.append('0')
            epsilon_rate.append('1')
        else:
            gamma_rate.append('1')
            epsilon_rate.append('0')
    
    return gamma_rate, epsilon_rate

def to_decimal(bit_list):
    return int(''.join(bit_list), 2)

def oxygen_rating(report, position):

    if len(report) == 1:
        print(report[0])
        return report[0]

    # get counts for the report
    counts = count_bits(report)
    counts_mask = ['1' if number >= 0 else '0' for number in counts]

    # filter out numbers that include most common bit at position
    filtered_report = []
    for number in report:
        if number[position] == counts_mask[position]:
            filtered_report.append(number)

    # use the filtered report to filter out next digit
    new_position = position + 1
    return oxygen_rating(filtered_report, new_position)


def carbon_rating(report, position):

    if len(report) == 1:
        return report[0]

    # get counts for the report
    counts = count_bits(report)
    counts_mask = ['1' if number >= 0 else '0' for number in counts]

    # filter out numbers that include most common bit at position
    filtered_report = []
    for number in report:
        if number[position] != counts_mask[position]:
            filtered_report.append(number)

    # use the filtered report to filter out next digit
    position += 1 
    return carbon_rating(filtered_report, position)


def main():
    report = read_input("inputs/day3.txt")
    counts = count_bits(report)
    gamma_rate, epsilon_rate = get_rates(counts)

    # print rates as binary
    print(f"{''.join(gamma_rate)}, {''.join(epsilon_rate)}")

    # convert to decimal
    gamma_rate = to_decimal(gamma_rate)
    epsilon_rate = to_decimal(epsilon_rate)
    print(f"{gamma_rate}, {epsilon_rate}, {gamma_rate * epsilon_rate}") # 177, 3918, 693486

    o2_rating = to_decimal(oxygen_rating(report, 0))
    co2_rating = to_decimal(carbon_rating(report, 0))

    print(f"{o2_rating}, {co2_rating}, {o2_rating * co2_rating}") # 933, 3622, 3379326

if __name__ == "__main__":
    main()