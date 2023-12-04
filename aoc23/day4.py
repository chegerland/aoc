#!/usr/bin/env python3
from collections import defaultdict


def main():

    # read file
    f = open("day4.txt", "r")
    file_content = f.read()

    cards = file_content.split("\n")

    # read all cards to parse information
    total = 0
    # key is card_id and value will be how many times we have that card
    cards_won = defaultdict(int)
    for card in cards:

        # parse info from line
        first_split = card.split(":")
        card_id = int(first_split[0].split()[-1])
        second_split = first_split[1].split("|")
        winning_numbers = second_split[0].split()
        picked_numbers = second_split[1].split()

        # part 1

        # check if numbers are winning numbers and calculate points
        points = 0
        num_cards_won = 0
        for picked_number in picked_numbers:
            if picked_number in winning_numbers:
                num_cards_won += 1

                if points == 0:
                    points = 1
                else:
                    points *= 2

        total += points

        # part 2
        cards_won[card_id] += 1

        # get new cards
        for j in range(1, cards_won[card_id]+1):  # for every card that we have
            for i in range(1, num_cards_won+1):  # add the following cards
                cards_won[card_id+i] += 1

    print(total)
    print(sum(cards_won.values()))


if __name__ == "__main__":
    main()
