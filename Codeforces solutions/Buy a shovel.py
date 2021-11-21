k, r = map(int, input().split(' '))

i = 0
error = [0, r]
remainder = (k * i) % 10

while remainder != r:
    i += 1
    remainder = (k * i) % 10
    if (k * i) % 10 == 0:
        print(i)
        exit(0)
print(i)
