with open("input/day2.txt", "r") as f:
    rounds = f.read().split("\n")

score = 0

for j in rounds:
    if j.startswith("A"):  # rock
        if j.endswith("Y"):  # draw
            score += 4  # 3+1
        if j.endswith("Z"):  # win
            score += 8  # 6+2
        if j.endswith("X"):  # loss
            score += 3  # 0+3

    if j.startswith("B"):  # paper
        if j.endswith("Y"):  # draw
            score += 5  # 3+2
        if j.endswith("Z"):  # win
            score += 9  # 6+3
        if j.endswith("X"):  # loss
            score += 1  # 0+1

    if j.startswith("C"):  # scissor
        if j.endswith("Y"):  # draw
            score += 6  # 3+3
        if j.endswith("Z"):  # win
            score += 7  # 6+1
        if j.endswith("X"):  # loss
            score += 2

print(score)
