t = int(input())

max_prices = []

for i in range(t):
    n = int(input())
    money = input().split(' ')
    money = [int(k) for k in money]
    money.sort()
    prices = []
    for j in range(len(money)):
        price = money[j]
        summa = 0
        for g in range(len(money)):
            if price <= money[g]:
                summa += price
        prices.append(summa)
    max_prices.append(max(prices))

for i in range(len(max_prices)):
    print(max_prices[i])
