n = int(input())
high = list(map(int, input().split(' ')))

t = 0

while high.index(max(high)) != 0:
    t += 1
    a = high[high.index(max(high))]
    b = high[high.index(max(high)) - 1]
    max_ind = high.index(max(high))
    high[max_ind - 1] = a
    high[max_ind] = b

high.reverse()

while high.index(min(high)) != 0:
    t += 1
    a = high[high.index(min(high))]
    b = high[high.index(min(high)) - 1]
    min_ind = high.index(min(high))
    high[min_ind - 1] = a
    high[min_ind] = b

print(t)

