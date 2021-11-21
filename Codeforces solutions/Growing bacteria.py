from math import log2
count = 0
k = 0
x = int(input())
while x:
    count += log2(x) // 1
    x -= 2**(log2(x) // 1)
    k += 1

print(k)
