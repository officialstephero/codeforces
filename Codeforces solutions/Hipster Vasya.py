import math

enter = list(map(int, input().split(' ')))

a = enter[0]
b = enter[1]

diff_days = min(a, b)
same_days = math.floor((max(a, b) - min(a, b)) / 2)

print(diff_days, same_days)
