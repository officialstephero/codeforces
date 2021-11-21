import math

n = int(input())

lucky_num = []

for i in range(n + 1):
    if len(str(i)) == (list(str(i)).count('4') + list(str(i)).count('7')):
        lucky_num.append(i)

k = 0
for num in lucky_num:
    if math.fmod(n, num) == 0:
        k += 1

if k > 0:
    print("YES")
else:
    print("NO")
