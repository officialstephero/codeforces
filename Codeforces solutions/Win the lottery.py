import math

n = int(input())
bills = [100, 20, 10, 5, 1]
k = 0

for bill in bills:
    k += math.floor(n / bill)
    n = math.fmod(n, bill)

print(k)
