import math

t = int(input())

n_chain = []

for i in range(t):
    n = int(input())
    if n > 2:
        n_chain.append(math.floor(int((n - 1) / 2)))
    else:
        n_chain.append(0)

for n in n_chain:
    print(n)



