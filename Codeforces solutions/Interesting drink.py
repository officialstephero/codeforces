n = int(input())
x = [int(i) for i in input().split()]
x_max = max(x)
q = int(input())
m = (int(input()) for _ in range(q))

count_fp = [0] * (x_max + 1)
for i in x:
    count_fp[i] += 1
for k in range(2, x_max + 1):
    count_fp[k] += count_fp[k - 1]

print(*[count_fp[j] if j < x_max else n for j in m], sep='\n')


