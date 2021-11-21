n = int(input())
t = list(map(int, input().split(' ')))

b = [0] * max(t)
for _ in t:
    b[_ - 1] += _

m = 0
s = 0
for k in b:
    m, s = max(m, k + s), m

print(m)
