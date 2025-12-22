import numpy as np
from collections import defaultdict

def get_inputs():
    with open("inputs/day7/real.txt") as f:
        lines = f.read().split("\n")
    grid = np.array([[char for char in line] for line in lines])
    return grid

def part1():
    grid = get_inputs()
    starting_position = np.nonzero(grid[0]=="S")[0].item()
    max_x_bound = grid.shape[0]
    max_y_bound = grid.shape[1]
    ray_positions = set([starting_position])
    curr_y = 0
    num_splits = 0
    while curr_y < max_y_bound:
        new_ray_positions = set()
        for ray in ray_positions:
            if grid[curr_y, ray] == "^":
                num_splits += 1
                if ray-1 >= 0:
                    new_ray_positions.add(ray-1)
                if ray+1 < max_x_bound:
                    new_ray_positions.add(ray+1)
            else:
                new_ray_positions.add(ray)
        ray_positions = new_ray_positions
        curr_y += 1
    print(num_splits)        


def part2():
    grid = get_inputs()
    starting_position = np.nonzero(grid[0]=="S")[0].item()
    max_x_bound = grid.shape[0]
    max_y_bound = grid.shape[1]
    ray_positions = defaultdict(lambda : defaultdict(lambda: 0))
    ray_positions[0][starting_position] = 1
    current_y = 0
    while current_y < max_y_bound:
        for ray in ray_positions[current_y]:
            if grid[current_y, ray] == "^":
                if ray-1 >= 0:
                    ray_positions[current_y+1][ray-1] += ray_positions[current_y][ray]
                if ray+1 < max_x_bound:
                    ray_positions[current_y+1][ray+1] += ray_positions[current_y][ray]
            else:
                ray_positions[current_y+1][ray] += ray_positions[current_y][ray]
        current_y += 1
    total_positions = 0
    for ray_y, possibilities in ray_positions[max_y_bound].items():
        total_positions += possibilities
    print(total_positions)


if __name__ == "__main__":
    part1()
    part2()