n = list(input())

syntax = "HQ9"

k = 0
for syn in list(syntax):
    if syn in n:
        k += 1

if k == 0:
    print("NO")
else:
    print("YES")
