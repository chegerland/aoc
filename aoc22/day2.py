#!/usr/bin/env python3

encoding = {
    "A": "Rock",
    "B": "Paper",
    "C": "Scissors",
    "X": "Rock",
    "Y": "Paper",
    "Z": "Scissors",
}

choice_value = {
    "Rock": 1,
    "Paper": 2,
    "Scissors": 3,
}

beats = {
    "Rock": "Scissors",
    "Paper": "Rock",
    "Scissors": "Paper",
}

loses_to = { v: k for k, v in beats.items() }

strategy = {
    "X": 0,
    "Y": 3,
    "Z": 6,
}

def get_round_score_1(enemy, player):
    player_enc = encoding[enemy]
    enemy_enc = encoding[player]
    if player_enc == enemy_enc:
        return 3
    elif beats[enemy_enc] == player_enc:
        return 6
    else:
        return 0

def get_round_score_2(enemy, player):

    score = 0

    if player == "X":
        score += choice_value[beats[encoding[enemy]]]
    elif player == "Y":
        score += choice_value[encoding[enemy]]
    elif player == "Z":
        score += choice_value[loses_to[encoding[enemy]]]

    return score + strategy[player]


def main():

    # read file
    f = open("inputs/day2.txt", "r")
    rounds = f.read().split("\n")

    total_score_1 = 0
    total_score_2 = 0
    for round in rounds: 
        players = round.split()
        enemy = players[0]
        player = players[1] 

        total_score_1 += get_round_score_1(enemy, player) + choice_value[encoding[player]]
        total_score_2 += get_round_score_2(enemy, player)
    

    print(total_score_1)
    print(total_score_2)
    

if __name__ == "__main__":
    main()