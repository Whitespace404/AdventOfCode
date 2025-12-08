from math import pow, sqrt

with open("test.txt") as f:
    rows = [i.rstrip() for i in f.readlines()]


def euclidean_distance_formula(x1, y1, z1, x2, y2, z2):
    a = pow((x2 - x1), 2)
    b = pow((y2 - y1), 2)
    c = pow((z2 - z1), 2)

    return sqrt(a + b + c)


rows = [row.split(",") for row in rows]

for i in range(len(rows) - 1):
    distances = []
    for j in range(len(rows) - 1):
        x1 = int(rows[i][0])
        y1 = int(rows[i][1])
        z1 = int(rows[i][2])

        x2 = int(rows[j][0])
        y2 = int(rows[j][1])
        z2 = int(rows[j][2])

        if i != j:
            distances.append((j, euclidean_distance_formula(x1, y1, z1, x2, y2, z2)))

    mini = distances[0][1]
    ind = distances[0][0]
    for k, distance in distances:
        if distance <= mini:
            mini = distance
            ind = k

    print(rows[ind], ind, sep="\t")
