with open("02.txt") as f:
    ranges = [i for i in f.read().split(",")]

answer = 0
for r in ranges:
    lower, higher = r.split("-")
    for i in range(int(lower), int(higher) + 1):
        left_half = str(i)[len(str(i)) // 2 :]
        right_half = str(i)[: len(str(i)) // 2]
        if left_half == right_half:
            answer += i

print(answer)
