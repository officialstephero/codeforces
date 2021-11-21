n = int(input())
m = list(map(int, input().split(' ')))
m.append(0)
k = 0
# s = 1
line = []

while k < len(m) - 1:
    s = 1
    while m[k] <= m[k + 1]:
        s += 1
        k += 1
    line.append(s)
    k += 1

print(max(line))
