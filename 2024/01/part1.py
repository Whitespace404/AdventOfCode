with open("input.txt", "r") as f:
    lines = [line.rstrip() for line in f.readlines()]
    lefts = []
    rights = []
    for line in lines:
        left, right = line.split()
        lefts.append(int(left))
        rights.append(int(right))

    total = 0
    for i in range(len(lefts)):
        sum_ = abs(sorted(lefts)[i] - sorted(rights)[i])
        total += sum_
    print(total)
