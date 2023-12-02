#!/usr/bin/env python3

def main():

    # read file
    f = open("day2.txt", "r")
    file_content = f.read()
    
    games = file_content.split("\n")

    # part 1

    allowed = {
        'red': 12,
        'green': 13,
        'blue': 14
    }

    # loop through game, some the possible game ids
    total = 0
    for game in games: 

        # split string to get info
        first_split = game.split(":")
        game_id = first_split[0].split()[-1]
        sets = first_split[1].split(";")

        game_is_possible = True

        # check the sets
        for set in sets: 
            cubes = set.split(",")

            for cube in cubes:
                num, type = cube.split()

                if int(num) > allowed[type]:
                    game_is_possible = False
            
            if not game_is_possible:
                break

        if game_is_possible:
            total += int(game_id) 

    print(total)

    # part 2

    # loop through game, some the possible game ids
    total = 0
    for game in games: 

        # split string to get info
        first_split = game.split(":")
        game_id = first_split[0].split()[-1]
        sets = first_split[1].split(";")

        # define minimum number of cubes needed
        min_cubes = {
            'red': 0,
            'green': 0,
            'blue': 0,
        }

        # check the sets
        for set in sets: 
            cubes = set.split(",")

            for cube in cubes:
                num, type = cube.split()

                if int(num) > min_cubes[type]:
                    min_cubes[type] = int(num)

        total += min_cubes['red'] * min_cubes["blue"] * min_cubes["green"] 

    print(total)



if __name__ == "__main__":
    main()