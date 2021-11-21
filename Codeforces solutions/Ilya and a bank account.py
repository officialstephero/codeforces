def min_bank(n):
    return max(int(n), int(n[:-1]), int(n[:-2] + n[-1]))


print(min_bank(input()))
