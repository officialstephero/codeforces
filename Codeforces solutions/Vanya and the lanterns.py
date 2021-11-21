n, s = map(int, input().split(' '))

a = list(map(int, input().split(' ')))
a = sorted(a)

max_len = 0

for i in range(n - 1):
    if (a[i + 1] - a[i]) > max_len:
        max_len = a[i + 1] - a[i]

print(f'{max(max_len / 2, a[0], s - a[-1]):.10f}')
