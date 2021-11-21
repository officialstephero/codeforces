enter = list(map(int, input().split(' ')))

n = enter[0]
k = enter[1]

t = 4 * 60
i = 0
time_comp = 5 * i
while k + time_comp <= t - 5 * (i + 1) and i != n:
    i += 1
    time_comp += 5 * i

print(i)
