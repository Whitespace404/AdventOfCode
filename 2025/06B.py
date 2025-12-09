with open("06.txt") as f:
    rows = f.readlines()

operations = rows.pop()
operations = operations.split()
answer = 0

mat = []
for i in range(len(rows[0])):
    operand = []
    for j in range(len(rows)):
        if not rows[j][i].isnumeric():
            continue
        operand.append(rows[j][i])

    number = ""
    for i in operand:
        if i == []:
            continue
        number = number + i
    mat.append(number)

mmap = []

local2 = []
for i in mat:
    if i == "":
        mmap.append(local2)
        local2 = []
    else:
        local2.append(i)


for i in range(len(mmap)):
    operation = operations[i]
    local_ans = 1
    for j in range(len(mmap[0])):
        if operation == "*":
            try:
                local_ans *= int(mmap[i][j])
            except IndexError:  # some lists may be shorter
                # but we are fine with that, just need to go onto the next
                pass

        elif operation == "+":
            try:
                local_ans += int(mmap[i][j])
            except IndexError:
                pass

    if operation == "+":
        local_ans -= 1
    answer += local_ans

print(answer)
