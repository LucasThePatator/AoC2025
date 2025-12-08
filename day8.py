from linecache import cache

import numpy as np
from functools import lru_cache

from numpy.ma.core import zeros_like


def parse_input(file_path: str):
    ret = []
    with open(file_path, 'r') as f:
        for line in f:
            if line == '\n':
                break
            ret.append(list(map(int, line.split(','))))

    return np.array(ret, dtype=np.uint64)

def compute_distance_list(vectors: np.array):
    distances = []
    for i in range(vectors.shape[0] - 1):
        for j in range(i + 1, vectors.shape[0]):
            dist2 = np.sum((vectors[i, :] - vectors[j, :]) ** 2)
            distances.append((dist2, (i, j)))

    distances.sort(key=lambda x: x[0])

    return distances

def one_star(file_path: str):
    vectors = parse_input(file_path)
    distances = compute_distance_list(vectors)
    circuit = np.arange(vectors.shape[0], dtype=np.uint64)

    for k in range(1000):
        i, j = distances[k][1]

        old_index = max(circuit[i], circuit[j])
        new_index = min(circuit[i], circuit[j])

        circuit[circuit == old_index] = new_index

    counts = []
    for c in range(vectors.shape[0]):
        counts.append(np.count_nonzero(circuit == c))

    counts.sort()
    print(counts[-1] * counts[-2] * counts[-3])


def two_star(file_path: str):
    vectors = parse_input(file_path)
    distances = compute_distance_list(vectors)

    circuit = np.arange(vectors.shape[0], dtype=np.uint64)
    k = 0
    while True:
        i, j = distances[k][1]

        old_index = max(circuit[i], circuit[j])
        new_index = min(circuit[i], circuit[j])

        circuit[circuit == old_index] = new_index

        if np.count_nonzero(circuit == 0) == vectors.shape[0]:
            print(vectors[i, 0] * vectors[j, 0])
            return

        k +=1

if __name__ == "__main__":
    two_star("data/day8")