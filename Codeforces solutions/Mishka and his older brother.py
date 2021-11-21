import math

masses = input()
masses = masses.split(' ')

a = int(masses[0])
b = int(masses[1])
n = 1

while (math.pow(3, n) * a) <= (math.pow(2, n) * b):
    n += 1

print(n)
