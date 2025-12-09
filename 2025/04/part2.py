with open("04.txt") as f:
    map = [bank.rstrip() for bank in f.readlines()]


def pad_input(mat):
    for i in range(len(mat)):
        mat[i] = list("-" + mat[i])
        mat[i].append("-")
    mat.insert(0, list("-" * len(mat[0])))
    mat.insert(len(mat), list("-" * len(mat[0])))

    return mat


map = pad_input(map)
answer = 0

indexes = [(0, 0)]
while indexes != []:
    indexes = []
    row = 1
    column = 1
    while row < len(map) - 1:
        column = 1
        while column < len(map[0]) - 1:
            surrounding_cells = [
                map[row + 1][column],
                map[row + 1][column + 1],
                map[row + 1][column - 1],
                map[row - 1][column],
                map[row - 1][column - 1],
                map[row - 1][column + 1],
                map[row][column + 1],
                map[row][column - 1],
            ]
            if map[row][column] == "@":
                if surrounding_cells.count("@") < 4:
                    indexes.append((row, column))
                    answer += 1
            column += 1
        row += 1
    for i, j in indexes:
        map[i][j] = "x"
print(answer)
