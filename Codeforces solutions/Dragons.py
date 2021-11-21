enter = list(map(int, input().split(' ')))
s = enter[0]
n = enter[1]

pair = []

for i in range(n):
    f = list(map(int, input().split(' ')))
    pair.append(f)

pair.sort()

for i in range(n):
    if pair[i][0] < s:
        s += pair[i][1]

    else:
        print('NO')
        exit(0)

print('YES')
