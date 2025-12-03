
def parse_input(file_path: str):
    ret = []
    with open(file_path, 'r') as f:
        for line in f:
            ret.append(int(line[:-1]))

    return ret

def one_star(file_path: str):
    data = parse_input(file_path)
    value = 0
    for number in data:
        s = str(number)
        n_list = list(map(int, s))
        first = max(n_list[:-1])
        first_i = n_list.index(first)
        second = max(n_list[first_i+1:])
        value += first * 10 + second

    print(value)

def two_star(file_path: str):
    data = parse_input(file_path)
    value = 0
    for number in data:
        s = str(number)
        n_list = list(map(int, s))
        output_list = []
        current_i = -1
        for i in range(12):
            end = len(n_list) if i == 11  else i - 11
            current = max(n_list[current_i+1:end])
            current_i = n_list[current_i+1:end].index(current) + current_i + 1
            output_list.append(current)

        voltage = int("".join(map(str, output_list)))
        value += voltage

    print(value)


if __name__ == "__main__":
    two_star("data/day3")