with open("input/day3.txt", "r") as f:
    bags = f.read().split("\n\n")

# common_items = []
# for bag in bags:
#     zip_a = set(bag[: (len(bag) // 2)])
#     zip_b = set(bag[(len(bag) // 2) :])
#     common_items.append(str(zip_a.intersection(zip_b)).lstrip("{'").rstrip("'}"))

lowercase = "abcdefghijklmnopqrstuvwxyz"
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

value_sheet = {}
init = 1
for letter in lowercase:
    value_sheet[letter] = init
    init += 1

init = 27
for letter_ in uppercase:
    value_sheet[letter_] = init
    init += 1

for team in bags:
    nl = team.split("\n")
    p = []
    for n in nl:
        p.append(set(n.split()))
    logo = p[0].intersection(p[1]).intersection(p[2])
    print(logo)

# score = 0
# for item in common_items:
#     score += value_sheet.get(item)
# print(score)
