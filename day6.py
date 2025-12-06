import numpy as np

def parse_input1(file_path: str):
    columns, operators = [], None
    with open(file_path, 'r') as f:
        s = f.read()
        lines = s.split('\n')

        for l in lines[0:-2]:
            columns.append(tuple(map(int, l.split())))

        operators = lines[-2].split()

    return np.array(columns), operators

def one_star(file_path: str):
    columns, operators = parse_input1(file_path)

    result = 0
    for i, op in enumerate(operators):
        if op == '*':
            result += np.multiply.reduce(columns[:, i])
        if op == '+':
            result += np.add.reduce(columns[:, i])

    print(result)

def parse_input2(file_path: str):
    columns, operators = [], None
    with open(file_path, 'r') as f:
        s = f.read()
        lines = s.split('\n')
        for l in lines[0:-2]:
            columns.append(list(l))

        operators = lines[-2].split()

    return np.array(columns, dtype=str), operators

def two_star(file_path: str):
    colums, operators = parse_input2(file_path)

    result = 0
    current_col_idx = 0
    for op in operators:
        numbers = []
        while True:
            if current_col_idx >= colums.shape[1]:
                break
                
            col = colums[:, current_col_idx]
            if np.all(col == ' '):
                current_col_idx += 1
                break
            
            numbers.append(int("".join(col).replace(" ", "")))
            current_col_idx += 1

        if op == '*':
            result += np.multiply.reduce(numbers)
        if op == '+':
            result += np.add.reduce(numbers)
                
    print(result)

if __name__ == "__main__":
    two_star("data/day6")