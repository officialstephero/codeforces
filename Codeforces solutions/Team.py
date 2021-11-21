n = int(input())
score = []
k = 0
for i in range(n):
    score = str(input())
    if score.count('1') >= 2:
        k += 1
print(k)


