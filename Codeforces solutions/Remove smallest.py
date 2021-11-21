t = int(input())

for k in range(t):
    n = int(input())
    a = list(map(int, input().split(' ')))
    counter = []
    a.sort()
    for i in range(n - 1):
        if 0 < (a[i] - a[i + 1]) <= 1:
            a[i + 1] = 0
        elif -1 <= (a[i] - a[i + 1]) < 0:
            a[i] = 0
        elif (a[i] - a[i + 1]) == 0:
            a[i] = 0

    counter.append(int(n - a.count(0)))

    if sum(counter) == 1 or n == 1:
        print('YES')
    else:
        print('NO')
