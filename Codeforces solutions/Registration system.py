n = int(input())

d = dict()
for i in range(n):
    s = input()
    d[s] = d.get(s, -1) + 1
    if d[s] == 0:
        print('OK')
    else:
        print(s, d[s], sep='')

