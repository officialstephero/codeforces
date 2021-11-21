t = int(input())
n = [int(input()) for _ in range(t)]

k = 2
x = [0]*t
while x.count(0) != 0:
    x = [int(n[i]/(2**k - 1)) if x[i] == 0 and n[i]/(2**k - 1) % 1 == 0 else x[i] for i in range(t)]
    k += 1

print(*x, sep='\n')
