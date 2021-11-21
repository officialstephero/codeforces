enter = list(map(int, input().split(' ')))
n = enter[0]    # количество проездов, запланированное Аней
m = enter[1]    # количество проездов, которое покрывает абонемент
a = enter[2]    # цена одного проезда
b = enter[3]    # цена одного абонемента

sub_count = n // m
other_count = n % m
print(min((sub_count + 1) * b, sub_count * b + other_count * a, n * a))
