n = int(input())

x = []
y = []
z = []

for i in range(n):
    k = input().split(' ')
    x.append(int(k[0]))
    y.append(int(k[1]))
    z.append(int(k[2]))

if ((sum(x) or sum(y)) or sum(z)) != 0:
    print('NO')
else:
    print('YES')
