n = int(input())
s = input().split(' ')
s.sort(reverse=True)
s = [int(i) for i in s]

max_taxi = 4
taxi = []

for k in range(n):
    s.sort(reverse=True)
    for i in range(len(s) - 1):
        if s[i] + s[i + 1] > max_taxi:
            pass
        else:
            s[i] = s[i] + s[i + 1]
            s[i + 1] = 0

for per in s:
    if per > 0:
        taxi.append(1)

print(len(taxi))
