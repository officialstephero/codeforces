options = input().split(' ')

n = int(options[0])
h = int(options[1])

friends = input().split(' ')

length = 0

for i in range(n):
    if h >= int(friends[i]):
        length += 1
    else:
        length += 2

print(length)
