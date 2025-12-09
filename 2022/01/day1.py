lines = []
with open("input/day1.txt", "r") as f:
    for line in f.readlines():
        try:
            lines.append(int(line))
        except ValueError:
            lines.append(" ")

sums_of_calories = []
sum = 0
for l in lines:
    if l != " ":
        sum += l
    else:
        sums_of_calories.append(sum)
        sum = 0

print(sums_of_calories)

for sum in sums_of_calories:
    if sum > 65339:
        print(sum)
