t = int(input())

for i in range(t):
    n = int(input())
    even = list(range(2, int(2 * n / 2) + 1, 2))
    odd = list(range(1, int(2 * n / 2) + 1, 2))
    if n not in range(2, n + 1, 4):
        diff = odd[-1] + sum(even) - sum(odd)
        print('YES')
        print(" ".join(map(str, even + odd[:-1])), diff)
    else:
        print('NO')
