def maximum(y, x):
    num = ''
    while x:
        if x >= 9:
            num += '9'
            x -= 9
        else:
            num += str(x)
            x = 0
    return int(f'{num:0<{y}}')


def minimum(y, x):
    num = ''
    support = str(x)
    while x:
        if x > 9:
            num += '9'
            x -= 9
        else:
            num += str(x - 1)
            support = str(x)
            x = 0
    num = f'1{num[::-1]:0>{y - 1}}'
    return int(num) if len(num) == y != 1 else int(support + num[2:])


m, s = map(int, input().split())
if 9 * m < s or (m > 1 and s == 0):
    print('-1 -1')
else:
    print(minimum(m, s), maximum(m, s))
