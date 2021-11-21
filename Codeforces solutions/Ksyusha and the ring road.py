enter = list(map(int, input().split(' ')))

n = enter[0]
m = enter[1]

a = list(map(int, input().split(' ')))

place = 1
steps = 0

for i in range(m):
    if place > n:
        place -= n

    if place < a[i]:
        steps += a[i] - place
        place += a[i] - place
    elif place == a[i]:
        continue
    elif place > a[i]:
        steps += n - (place - a[i])
        place += n - (place - a[i])

print(steps)

