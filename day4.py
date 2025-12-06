from scipy.ndimage import convolve
import numpy as np

INPUT_MAP = {
    ".": 0,
    "@": 1
}

def get_inputs():

    with open("inputs/day4/real.txt") as f:
        lines = f.readlines()
        lines = [[INPUT_MAP[c] for c in line.strip()] for line in lines]
    return np.array(lines)

def part1():
    inputs = get_inputs()
    weights = np.array(
        [
            [1, 1, 1],
            [1, 0, 1],
            [1, 1, 1]
        ]
    )
    n_neighbors = convolve(inputs, weights, mode="constant", cval=0)
    can_access = (n_neighbors < 4) & (inputs)
    print(can_access.sum())

def part2():
    current = get_inputs()
    weights = np.array(
        [
            [1, 1, 1],
            [1, 0, 1],
            [1, 1, 1]
        ]
    )
    can_evolve = True
    total_removed = 0
    while can_evolve:
        n_neighbors = convolve(current, weights, mode="constant", cval=0)
        can_access = (n_neighbors < 4) & (current)
        total_removed += can_access.sum()
        new = current - can_access
        if (new == current).all():
            can_evolve = False
        current = new
    print(total_removed)

if __name__ == "__main__":
    # part1()
    part2()