n = int(input())
color = input()
k = 0
for i in range(n - 1):
    if color[i] == color[i + 1]:
        k += 1
print(k)
