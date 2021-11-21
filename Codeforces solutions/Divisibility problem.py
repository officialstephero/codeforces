n = int(input())

raz = []

for i in range(n):
    numb = list(map(int, input().split(' ')))
    if numb[0] % numb[1] != 0:
        raz.append(numb[1] - numb[0] % numb[1])
    else:
        raz.append(0)

for dif in raz:
    print(dif)
