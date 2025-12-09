with open("06.txt") as f:
    rows = [i.rstrip() for i in f.readlines()]

operations = rows.pop()
operations = operations.split()

mrows = [i.split() for i in rows]

k = 0
answer = 0

correct_order = []
while k < len(mrows[0]):
    local_ans = 1
    operation = operations[k]
    for i in range(len(mrows)):
        if operation == "+":
            local_ans += int(mrows[i][k])
        elif operation == "*":
            local_ans *= int(mrows[i][k])
    if operation == "+":  # to account for the off-by-one :p
        answer -= 1
    answer += local_ans
    k += 1

print(answer)
