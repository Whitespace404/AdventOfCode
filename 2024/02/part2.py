with open("input.txt") as f:
    lines = []
    for i in f.read().splitlines():
        lines.append(i)


def is_safe(L):
    if all([L[i] > L[i + 1] for i in range(len(L) - 1)]) or all(
        [L[i] < L[i + 1] for i in range(len(L) - 1)]
    ):
        if all([abs(L[i + 1] - L[i]) <= 3 for i in range(len(L) - 1)]):
            return True
    return False


answer = 0
for line in lines:
    L = line.split(" ")
    L = [int(i) for i in L]

    for i in range(len(L)):
        if is_safe(L):
            answer += 1
            break
        L_prime = L.pop(i)

        if is_safe(L):
            answer += 1
            break
        L.insert(i, L_prime)

print(answer)
