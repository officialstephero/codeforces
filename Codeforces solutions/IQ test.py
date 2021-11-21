n = int(input())
numbers = list(map(int, input().split(' ')))

for i in range(1, n - 1):
    if ((numbers[i] - numbers[i - 1]) % 2 == 0) and ((numbers[i] - numbers[i + 1]) % 2 != 0):
        print(i + 2)
        break
    if ((numbers[i] - numbers[i - 1]) % 2 != 0) and ((numbers[i] - numbers[i + 1]) % 2 == 0):
        print(i)
        break
    if ((numbers[i] - numbers[i - 1]) % 2 != 0) and ((numbers[i] - numbers[i + 1]) % 2 != 0):
        print(i + 1)
        break
