n = int(input())
num_friend = input().split(' ')
alien = {}

for i in range(len(num_friend)):
    a = int(num_friend[i])
    alien[a] = num_friend.index(num_friend[i]) + 1

line = []
k = 0

for i in range(n):
    k += 1
    line.append(alien.get(k))

line = [str(i) for i in line]
print(' '.join(line))
