from itertools import count

import numpy as np

def parse_input(file_path: str):
    ranges, ids = [], []
    with open(file_path, 'r') as f:
        s = f.read()
        s_r, s_id = s.split('\n\n')

        for r in s_r.split('\n'):
            ranges.append(tuple(map(int, r.split('-'))))

        for id in s_id.split('\n'):
            ids.append(int(id))

    return ranges, ids

def one_star(file_path: str):
    ranges, ids = parse_input(file_path)
    count = 0
    for id in ids:
        for r in ranges:
            if r[0] <= id <= r[1]:
                count += 1
                break
    print(count)

def two_star(file_path: str):
    ranges, _ = parse_input(file_path)

    new_ranges = {ranges[0]}
    for r in ranges[1:]:
        intersecting_min = r[0]
        intersecting_max = r[1]
        to_remove = set()
        for nr in new_ranges:
            if nr[0] <= r[0] <= nr[1] or nr[0] <= r[1] <= nr[1] or (nr[0] >= r[0] and nr[1] <= r[1]):
                intersecting_min = min(nr[0], intersecting_min)
                intersecting_max = max(nr[1], intersecting_max)

                to_remove.add(nr)

        new_ranges -= to_remove
        add_range = (intersecting_min, intersecting_max)
        new_ranges.add(add_range)

    count = 0
    for nr in new_ranges:
        count+= nr[1] - nr[0] + 1

    print(count)

if __name__ == "__main__":
    two_star("data/day5")