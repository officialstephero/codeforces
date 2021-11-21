n = int(input())
s = input()
s = s.lower()
k = 0

for i in range(97, 123):
    if chr(i) in s:
        k += 1
    else:
        break
if k == 123 - 97:
    print('YES')
else:
    print('NO')
