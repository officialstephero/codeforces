n = int(input())
parses = list(map(int, input().split(' ')))
parses.sort(reverse=True)

summa = 0
k = 0

for i in range(n):
    if summa <= sum(parses[i:]):
        summa += parses[i]
        k += 1

print(k)

