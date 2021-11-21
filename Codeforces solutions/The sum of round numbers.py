t = int(input())

for i in range(t):
    n = int(input())
    terms = []
    for k in range(4, 0, -1):
        terms.append(n // (10 ** k) * (10 ** k))
        n %= (10 ** k)
    terms.append(n)
    sort = []
    for num in terms:
        if num != 0:
            sort.append(str(num))
    print(len(sort))
    print(" ".join(sort))
