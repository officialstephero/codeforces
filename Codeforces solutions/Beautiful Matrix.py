import math

for i in range(5):
    line = str(input())
    line = line.split(' ')

    if '1' in line:
        a = i + 1
        b = 1 + line.index('1')
n = math.fabs(3 - a) + math.fabs(3 - b)
print(int(n))
