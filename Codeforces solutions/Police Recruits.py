n = int(input())
t = list(map(int, input().split(' ')))

k = 0
count = 0

for i in range(n):
    if t[i] < 0 and k == 0:
        count += 1
    elif (t[i] < 0) and (k > 0):
        k += t[i]
    elif t[i] > 0:
        k += t[i]

print(count)
