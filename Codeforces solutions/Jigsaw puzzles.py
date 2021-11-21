n = list(map(int, input().split(' ')))
f = list(map(int, input().split(' ')))
f = sorted(f)

dif = []

for i in range(n[1] - n[0] + 1):
    p = f[i:n[0] + i]
    dif.append(p[-1] - p[0])

print(min(dif))
