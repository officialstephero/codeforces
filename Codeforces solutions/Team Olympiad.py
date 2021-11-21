n = int(input())
t = list(map(int, input().split(' ')))

d = sorted(list(zip(t, range(1, n+1))))
one = [p[1] for p in d if p[0] == 1]
two = [p[1] for p in d if p[0] == 2]
three = [p[1] for p in d if p[0] == 3]

print(min(len(one), len(two), len(three)))
i = 0
while one and two and three:
    print(f'{one.pop(i)} {two.pop(i)} {three.pop(i)}')










