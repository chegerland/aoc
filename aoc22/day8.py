#!/usr/bin/env python3
import numpy as np

def main():

    f = open("inputs/day8.txt", "r")
    grid = np.array([[int(tree) for tree in line] for line in f.read().split("\n")])
    grid_size = grid.shape[0]
    
    visible = np.zeros(shape=(grid_size, grid_size), dtype=int)
    viewing_distance = np.zeros(shape=(grid_size, grid_size), dtype=int)

    for x, y in np.ndindex(grid.shape):

        # get all directions, flip left and top so we can loop better 
        left = np.flip(grid[x, :y])
        right = grid[x, y+1:]
        top = np.flip(grid[:x, y])
        bottom = grid[x+1:, y]
        directions = [left, right, top, bottom]

        # edges are visible
        if x == 0 or x == grid_size - 1 or y == 0 or y == grid_size - 1:
            visible[x][y] = 1

        scenic_score = 1
        for direction in directions:
            if np.all(direction < grid[x][y]):
                visible[x][y] = 1

            scenic_score_direction = 0
            for tree in direction:
                scenic_score_direction += 1
                if tree >= grid[x][y]:
                    break

            scenic_score *= scenic_score_direction

        viewing_distance[x][y] = scenic_score

    print(f"Answer 1: {visible.sum()}")
    print(f"Answer 2: {viewing_distance.max()}")


if __name__ == "__main__":
    main()
