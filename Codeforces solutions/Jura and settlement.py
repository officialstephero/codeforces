n = int(input())

count = 0

for i in range(n):
    room = input().split(' ')
    if (int(room[1]) - int(room[0])) >= 2:
        count += 1

print(count)
