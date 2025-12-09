with open("09.txt") as f:
    rows = [i.rstrip() for i in f.readlines()]

answer = 0

for i in rows:
    x1, y1 = i.split(",")
    for j in rows:
        x2, y2 = j.split(",")
        area = ((int(y2) - int(y1)) + 1) * (int(x2) - int(x1) + 1)
        if area > answer:
            answer = area

print(answer)
