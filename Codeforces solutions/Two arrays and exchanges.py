def sum_exchanges(a, b, c):
    k = int(a[1])
    while k:
        if max(c) > min(b):
            b[b.index(min(b))] = max(c)
            c.remove((max(c)))
        k -= 1

    return sum(b)


t = int(input())
for i in range(t):
    print(sum_exchanges(list(map(int, input().split(' '))),
                        list(map(int, input().split(' '))),
                        list(map(int, input().split(' ')))))
