n = input()
n += ' '

row_n = []

for i in range(len(n) - 1):
    if n[i] == n[i + 1]:
        row_n.append(n[i])
    else:
        row_n.append(n[i])
        row_n.append(' ')

del row_n[-1]

row_n = "".join(row_n)
row_n = row_n.split(' ')

maximum = 0
for el in row_n:
    if len(el) > maximum:
        maximum = len(el)

if maximum >= 7:
    print("YES")
else:
    print("NO")
