with open("test.txt") as f:
    ranges, nos = f.read().split("\n\n")

R = [(i.split("-")) for i in ranges.split("\n")]

answer = 0
checked_ranges = []


def check_n_in_ranges(i, R):
    for lower, upper in R:
        if i >= int(lower) and i <= int(upper):
            return True
    return False
