import math

n = list(map(int, input().split(' ')))

if math.fmod(n[0], 2) != 0:
    n[0] += 1

if n[1] <= int(n[0] / 2):
    print(int(2 * n[1] - 1))
else:
    print(int(2 * (n[1] - n[0] / 2)))
