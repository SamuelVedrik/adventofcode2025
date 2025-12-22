from sklearn.metrics import pairwise_distances
from scipy.cluster.hierarchy import DisjointSet
import numpy as np

NUM_PAIRS = 1000

def get_inputs():
    with open("inputs/day8/real.txt") as f:
        data = [line.strip().split(",") for line in f.readlines()]
        return np.array(data).astype(float)

def part1():
    points = get_inputs()
    as_tuples = [tuple(row) for row in points]
    distances = pairwise_distances(points)
    modified_distances = np.where(np.tril(distances) == 0, np.inf, distances)
    sorted_indices = np.unravel_index(np.argsort(modified_distances, axis=None), modified_distances.shape)
    to_connect = np.c_[sorted_indices[0][:NUM_PAIRS], sorted_indices[1][:NUM_PAIRS]]
    sets = DisjointSet(as_tuples)
    for row in to_connect:
        sets.merge(as_tuples[row[0]], as_tuples[row[1]])
    sizes = sorted([len(subset) for subset in sets.subsets()])
    print(sizes[-1] * sizes[-2] * sizes[-3])

def part2():
    points = get_inputs()
    as_tuples = [tuple(row) for row in points]
    distances = pairwise_distances(points)
    modified_distances = np.where(np.tril(distances) == 0, np.inf, distances)
    sorted_indices = np.unravel_index(np.argsort(modified_distances, axis=None), modified_distances.shape)
    to_connect = np.c_[sorted_indices[0], sorted_indices[1]]
    sets = DisjointSet(as_tuples)
    last_pairs = None, None
    curr_index = 0
    while len(sets.subsets()) > 1:
        merge_a = as_tuples[to_connect[curr_index][0]]
        merge_b = as_tuples[to_connect[curr_index][1]]
        sets.merge(merge_a, merge_b)
        last_pairs = merge_a, merge_b
        curr_index += 1
    print(last_pairs[0][0] * last_pairs[1][0])



if __name__ =="__main__":
    # part1()
    part2()
    