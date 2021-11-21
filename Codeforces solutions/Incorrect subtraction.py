import math

ent = input()
ent = ent.split(' ')

n = int(ent[0])
k = int(ent[1])

for i in range(k):
    if math.fmod(n, 10) == 0:
        n = int(n / 10)
    else:
        n -= 1

print(n)
