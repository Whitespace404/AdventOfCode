with open("04.txt") as f:
    map = [bank.rstrip() for bank in f.readlines()]


def pad_input(mat):
    for i in range(len(mat)):
        mat[i] = "-" + mat[i]
        mat[i] = mat[i] + "-"
    mat.insert(0, "-" * len(mat[0]))
    mat.insert(len(mat), "-" * len(mat[0]))

    return mat


row = 1
column = 1
counts = []
map = pad_input(map)

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
            counts.append(surrounding_cells.count("@"))
        column += 1
    row += 1

print(sum([1 for i in counts if i < 4]))
