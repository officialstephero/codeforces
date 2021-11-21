n = int(input())

points = list(map(int, input().split(' ')))

k = 0

for i in range(1, n):
    if points[i] < min(points[:i])\
            or points[i] > max(points[:i]):
        k += 1

print(k)
