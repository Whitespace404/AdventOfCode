with open("test.txt") as f:
    instructions = [L.rstrip() for L in f.readlines()]

answer = 0
current_index = 50

for i in instructions:
    direction = i[0]
    local_ans = 0
    clicks = int(i.lstrip(direction))
    print(current_index, "\t", i, end="\t")

    if clicks >= 100:
        local_ans += clicks // 100
        clicks = clicks % 100

    if direction == "L":
        if clicks <= current_index:
            current_index -= clicks
        elif clicks > current_index:
            if current_index != 0:
                local_ans += 1
            current_index = abs(100 + (current_index - clicks))

    elif direction == "R":
        if clicks + current_index == 100:
            current_index = 0

        elif clicks + current_index <= 99:
            current_index += clicks
        else:
            if current_index != 0:
                local_ans += 1
            current_index = abs(100 - (current_index + clicks))

    print(f"after rotating {i}", local_ans)
    answer += local_ans
print(answer)  # this does not include when it ends up AT 0
# add answer from part 1 to get final answer
