year = int(int(input()))

summa = 0

while summa != len(str(year)):
    summa = 0
    year += 1
    year_l = list(str(year))
    for i in range(len(year_l)):
        count = year_l.count(year_l[i])
        summa += count

print(year)
