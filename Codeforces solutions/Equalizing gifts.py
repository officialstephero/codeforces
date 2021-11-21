for _ in range(int(input())):
    n, a, b = int(input()), list(map(int, input().split())), list(map(int, input().split()))
    print(sum((max(x, y) for x, y in zip((x - min(a) for x in a), (x - min(b) for x in b)))))
