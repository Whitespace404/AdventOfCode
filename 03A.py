with open("03.txt") as f:
    banks = [bank.rstrip() for bank in f.readlines()]

answer = 0
for bank in banks:
    largest_possible_value = int(bank[0])

    for i in range(len(bank)):
        for j in range(len(bank)):
            if int(bank[i] + bank[j]) > largest_possible_value and i < j:
                largest_possible_value = int(bank[i] + bank[j])

    answer += largest_possible_value

print(answer)
