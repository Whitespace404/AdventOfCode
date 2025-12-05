with open("05.txt") as f:
    ranges, nos = f.read().split("\n\n")

R = [(i.split("-")) for i in ranges.split("\n")]
N = [int(i) for i in nos.split("\n")]

answer = 0

for i in N:
    for lower, upper in R:
        if i >= int(lower) and i <= int(upper):
            answer += 1
            break
print(answer)
