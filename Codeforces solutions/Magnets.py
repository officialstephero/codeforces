n = int(input())
line = []

for i in range(n):
    line.append(input())

line = "".join(line)
print(line.count('11') + line.count('00') + 1)
