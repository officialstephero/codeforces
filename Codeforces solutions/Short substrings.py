n = int(input())

for i in range(n):
    t = list(input())
    for k in range(1, len(t) - 1, 2):
        if t[k] == t[k + 1]:
            t[k] = ''

    print("".join(t))
