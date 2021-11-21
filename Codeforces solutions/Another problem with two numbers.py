t = int(input())

for i in range(t):
    a, b = map(int, input().split(' '))
    c = max(a, b) - min(a, b)
    count = 0

    for k in range(10, 0, -1):
        count += c // k
        c -= k * (c // k)

    print(count)

