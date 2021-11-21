levels = int(input())
lit_x = list(map(int, input().split(' ')))
lit_y = list(map(int, input().split(' ')))

lit_x.pop(0)
lit_y.pop(0)

summa = 0

while levels != 0:
    summa += levels
    levels -= 1

if sum(set.union(set(lit_x), set(lit_y))) == summa:
    print('I become the guy.')
else:
    print('Oh, my keyboard!')
