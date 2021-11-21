import math

x = int(input())
count = []

for i in range(5, 0, -1):
    k = 0
    while math.floor(x / i) != 0:
        x -= i
        k += 1
    count.append(k)

print(sum(count))
