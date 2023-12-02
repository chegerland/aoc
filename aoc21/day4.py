import numpy as np


def read_input(filename):
    blocks = []
    with open(filename) as file:
        number_list = file.readline().split(',')
        number_list[-1] = number_list[-1].split()[0]
        number_list = [int(num) for num in number_list]
        file.readline()

        current_block = []
        for line in file:
            if line != "\n":
                current_block.append([int(num) for num in line.split()])
            else:
                blocks.append(np.array(current_block))
                current_block = []
    
    return number_list, blocks

def is_number_in_list(list, number):
    if number in list:
        return 1
    else:
        return 0

def get_masked_block(number_list, block):
    lamb = lambda x: is_number_in_list(number_list, x)
    return np.vectorize(lamb)(block)

def check_for_win(block):
    row_sum = np.sum(block, axis=1)
    column_sum = np.sum(block, axis=0)
    if np.any(row_sum == 5):
        return True
    elif np.any(column_sum == 5):
        return True
    else:
        return False


def play_bingo(number_list, blocks):
    for i in range(5, len(number_list)):
        for block in blocks:
            # get a masked block
            masked_block = get_masked_block(number_list[:i], block)

            # check if its the winning one
            if check_for_win(masked_block):
                return i-1, block
            else:
                #print(f"No win after {i} rounds.")
                pass


def play_bingo_2(number_list, blocks):
    wins_after_round = []

    # for each block: get the number of rounds after which the block will win
    for block in blocks:
        for i in range(5, len(number_list)):
            # get a masked block
            masked_block = get_masked_block(number_list[:i], block)

            # check if the block wins
            if check_for_win(masked_block):
                wins_after_round.append(i)
                break

    print(wins_after_round)
    
    loosing_block = blocks[np.argmax(wins_after_round)] 
    return np.max(wins_after_round) - 1, loosing_block

def sum_of_unmarked_numbers(marked_numbers, winning_block):
    def is_in_list(list, number):
        if number in list:
            return 0
        else:
            return number
    
    lamb = lambda x: is_in_list(marked_numbers, x)
    block = np.vectorize(lamb)(winning_block)
    print(block)

    return block.sum()


def main():
    number_list, blocks = read_input("inputs/day4.txt")
    index, winning_block = play_bingo(number_list, blocks)

    # first task
    number = number_list[index]
    sum = sum_of_unmarked_numbers(number_list[:index+1], winning_block)
    #print(f"Sum: {sum}, Number called: {number}, Solution: {sum * number}")

    print("\n")

    # second task
    index, loosing_block = play_bingo_2(number_list, blocks)
    print(index)
    print(loosing_block)
    number = number_list[index]
    print(number)
    sum = sum_of_unmarked_numbers(number_list[:index+1], loosing_block)
    print(f"Sum: {sum}, Number called: {number}, Solution: {sum * number}")


if __name__ == "__main__":
    main()