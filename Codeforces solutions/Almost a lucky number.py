number = input()
number = list(number)

four = number.count('4')
seven = number.count('7')

if (four + seven == 4) or (four + seven == 7):
    print('YES')
else:
    print('NO')
