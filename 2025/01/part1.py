with open("01.txt") as f:
    instructions = [L.rstrip() for L in f.readlines()]


def traverse_left(current_index, count):
    Delta = current_index - count
    return Delta if Delta >= 0 else abs(100 + Delta)


def traverse_right(current_index, count):
    Delta = current_index + count
    return Delta if Delta <= 99 else abs(100 - Delta)


answer = 0
current_index = 50
for i in instructions:
    count = int(i[1:])
    if count >= 100:
        count = int(i[-2:])
    if i.startswith("L"):
        current_index = traverse_left(current_index, count)
    else:
        current_index = traverse_right(current_index, count)
    if current_index == 0:
        answer += 1
print(answer)
