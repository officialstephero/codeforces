enter = list(map(int, input().split(' ')))

s = enter[0]
m = enter[1]

for i in range(1, (s + 1)):
    if i in range(1, (s + 1), 2):
        print('#' * m)
    elif i in range(2, (s + 1), 4):
        print('.' * (m - 1) + '#')
    else:
        print('#' + '.' * (m - 1))
