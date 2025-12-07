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

    maxi = []
    while len(maxi) <= 12:
        i = 9
        while i > 0:
            j = 0
            while j < len(joltage):
                if (
                    joltage[j] == i
                    and len(maxi) < 12
                    and len(joltage[joltage.index(i) :]) >= (11 - len(maxi))
                ):
                    maxi.append(joltage[j])
                    i = 9
                    del joltage[0 : j + 1]
                    j = 0
                    break
                j += 1
            i -= 1
    print(maxi)
    # s = [str(i) for i in maxi]
    # A = ""
    # for i in s:
    #     A = A + i
    # answer += int(A)
    # print(int(A))

# 9876543211111 987654321111
# 8111111111111 811111111119
# 4444333222888 434234234278
# 8881111111111 888911112111
