def transport(a, b):
    position = 1
    while position < a[1]:
        position += b[position - 1]
        if position == a[1]:
            return 'YES'
    return 'NO'


print(transport(list(map(int, input().split(' '))),
                list(map(int, input().split(' ')))))
