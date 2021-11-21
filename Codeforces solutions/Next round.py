places = input()
places = places.split(' ')

points = input()
points = points.split(' ')

d = 0
k = points[int(places[1]) - 1]
points.reverse()
for i in range(int(places[0])):
    if float(points[i]) < float(k) or float(points[i]) == 0:
        d += 1
    else:
        d = d
print(len(points) - d)
