import numpy as np

def parse_input(file_path: str):
    ret = []
    with open(file_path, 'r') as f:
        for line in f:
            ret.append([1 if c == '@' else 0 for c in line[:-1]])

    return np.array(ret)

def count_adjacent(arr: np.array, x: int, y: int):
    count = 0
    if x > 0:
        count += arr[x-1, y]
        if y > 0:
            count += arr[x-1, y-1]
        if y < arr.shape[1]-1:
            count += arr[x-1, y+1]

    if x < arr.shape[0]-1:
        count += arr[x+1, y]
        if y > 0:
            count += arr[x+1, y-1]

        if y < arr.shape[1]-1:
            count += arr[x+1, y+1]

    if y > 0:
        count += arr[x, y-1]

    if y < arr.shape[1]-1:
        count += arr[x, y+1]

    return count

def one_star(file_path: str):
    data = parse_input(file_path)
    count = 0
    for x in range(0, data.shape[0]):
        for y in range(0, data.shape[1]):
            if data[x, y] == 1 and count_adjacent(data, x, y) < 4:
                count += 1
    print(count)

def two_star(file_path: str):
    data = parse_input(file_path)
    total_count = 0
    count = 1
    while count > 0:
        new_data = np.copy(data)
        count = 0
        for x in range(0, data.shape[0]):
            for y in range(0, data.shape[1]):
                if data[x, y] == 1 and count_adjacent(data, x, y) < 4:
                    count += 1
                    new_data[x, y] = 0

        data = np.copy(new_data)

        total_count += count

    print(total_count)

if __name__ == "__main__":
    two_star("data/day4")