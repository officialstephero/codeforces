for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    even = [1 if i % 2 == 0 and a[i] % 2 != 0 else -1 if i % 2 != 0 and a[i] % 2 == 0 else 0 for i in range(len(a))]
    if sum(even) == 0:
        print(even.count(1))
    else:
        print(-1)

