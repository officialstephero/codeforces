import math

sides = input()
sides = sides.split(' ')
for i in range(len(sides)):
    sides[i] = int(sides[i])
perimeter = sides[0] * sides[1]
count = math.floor(perimeter / 2)
print(count)
