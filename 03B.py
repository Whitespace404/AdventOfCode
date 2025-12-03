from itertools import combinations

with open("test.txt") as f:
    banks = [bank.rstrip() for bank in f.readlines()]


def remove_last_occurence(List, element):
    for i in range(len(List) - 1, -1, -1):
        if List[i] == element:
            del List[i]
            break
    return List


answer = 0
for bank in banks:
    joltage = list(int(i) for i in bank)

    i = 1
    while len(joltage) != 12:
        while joltage.count(i) != 0 and len(joltage) != 12:
            joltage = remove_last_occurence(joltage, i)
        i += 1

    # converting maximum possible joltage of this bank from list to string
    sjolt = ""
    for i in joltage:
        sjolt += str(i)
    print(sjolt)
    answer += int(sjolt)

print(answer)
