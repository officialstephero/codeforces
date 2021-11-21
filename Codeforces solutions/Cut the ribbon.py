import itertools


enter = list(map(int, input().split(' ')))

n = enter[0]
a = enter[1]
b = enter[2]
c = enter[3]

f = [0] + [-4001] * 4000

for i in range(1, n+1):
    f[i] = max(f[i-a], f[i-b], f[i-c]) + 1

print(f[n])
