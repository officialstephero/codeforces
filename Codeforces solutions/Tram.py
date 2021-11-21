n = int(input())
counts = []
count = 0
for i in range(n):
    passengers = input()
    passengers = passengers.split(' ')
    a = int(passengers[0])
    b = int(passengers[1])
    count += (b - a)
    counts.append(count)
print(max(counts))
