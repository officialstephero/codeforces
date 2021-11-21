def equality(a):
    a = [max(a) - p for p in a]
    return sum(a)


n = int(input())
a = list(map(int, input().split(' ')))

print(equality(a))
