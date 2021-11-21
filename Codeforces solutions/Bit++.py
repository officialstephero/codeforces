n = input()
operations = []
for i in range(int(n)):
    k = input()
    operations.append(k)
operations = "".join(operations)
plus = operations.count('++')
minus = operations.count('--')
x = plus - minus
print(x)
