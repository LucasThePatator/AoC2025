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
            ret.append([{'.' : 0,
                         '^' : 1,
                         'S' : 2}[c]
                        for c in line[:-1]])

    return np.array(ret, dtype=np.uint8)

def one_star(file_path: str):

    splits = 0
    table = parse_input(file_path)
    for i in range(table.shape[0] - 1):
        for j in range(table.shape[1]):
            if table[i, j] != 2:
                continue

            if table[i+1, j] == 0:
                table[i+1, j] = 2

            if table[i+1, j] == 1:
                splits += 1
                if j-1 >= 0:
                    table[i+1, j-1] = 2
                if j+1 < table.shape[1]:
                    table[i+1, j+1] = 2

    print(splits)


def two_star(file_path: str):
    table = parse_input(file_path)
    counts = zeros_like(table, dtype=np.uint64)

    tachyon_start_pos = np.argwhere(table[0, :] == 2)
    counts[0, tachyon_start_pos] = 1

    for i in range(table.shape[0] - 1):
        for j in range(table.shape[1]):
            if counts[i, j] == 0:
                continue

            if table[i + 1, j] == 0:
                counts[i + 1, j] += counts[i, j]

            if table[i + 1, j] == 1:
                if j - 1 >= 0:
                    counts[i + 1, j - 1] += counts[i, j]
                if j + 1 < table.shape[1]:
                    counts[i + 1, j + 1] += counts[i, j]

    print(sum(counts[-1, :]))

if __name__ == "__main__":
    two_star("data/day7")