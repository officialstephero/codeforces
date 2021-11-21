def team_selection(k, y):
    y = [p+k for p in y if p+k <= 5]
    return f'{len(y)//3:.0f}'


n, k = map(int, input().split(' '))
y = list(map(int, input().split(' ')))

print(team_selection(k, y))
