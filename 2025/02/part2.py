with open("02.txt") as f:
    ranges = [i for i in f.read().split(",")]


def check_repetitons(word):
    word = str(word)
    for j in range(1, len(word)):
        if len(word) == word.count(word[0:j]) * len(word[0:j]):
            return True
    return False


answer = 0
for r in ranges:
    lower, higher = r.split("-")
    for i in range(int(lower), int(higher) + 1):
        if check_repetitons(str(i)):
            answer += i

print(answer)
