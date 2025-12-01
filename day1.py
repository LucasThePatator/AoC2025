
def mod(a, b):
    return (a % b + b) % b

def one_star(file_path: str):

    count = 0
    value = 50
    with open(file_path, 'r') as f:
        for line in f:
            direction = line[:1]
            add = int(line[1:-1])
            if direction == 'L':
                value = mod(value - add, 100)
            if direction == 'R':
                value = mod(value + add, 100)
            if value == 0:
                count += 1

    print(f"count: {count}")

def two_star(file_path: str):
    count = 0
    value = 50
    with open(file_path, 'r') as f:
        for line in f:
            direction = line[:1]
            add = int(line[1:-1])

            if direction == 'L':
                diff = value - add
                if diff < 0:
                    count += (add - value) // 100
                    if value > 0:
                        count += 1

                if diff == 0:
                    count += 1

                value = mod(diff, 100)

            if direction == 'R':
                count += (value + add) // 100
                value = mod(value + add, 100)

            print(f"count: {count}")

if __name__ == "__main__":
    two_star("data/day1")