
def parse_input(file_path: str):
    ret = []
    with open(file_path, 'r') as f:
        s1 = f.read().split(',')
        for line in s1:
            a, b = line.split('-')
            ret.append((int(a), int(b)))

    return ret

def one_star(file_path: str):
    data = parse_input(file_path)
    value = 0
    for a, b in data:
        for number in range(a, b+1):
            s = str(number)
            l = len(s)
            if len(s) % 2 == 1:
                continue

            if s[:l//2] == s[l//2:]:
                value += number

    print(value)

def two_star(file_path: str):
    data = parse_input(file_path)
    value = 0
    for a, b in data:
        for number in range(a, b+1):
            s = str(number)
            l = len(s)
            for d in range(1, l//2 + 1):
                if l % d != 0:
                    continue
                if s == s[:d] * (l//d):
                    value += number
                    break


    print(value)


if __name__ == "__main__":
    two_star("data/day2")