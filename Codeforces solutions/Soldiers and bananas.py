options = input()
options = options.split(' ')

k = int(options[0])
n = int(options[1])
w = int(options[2])
price = 0

for i in range(w):
    price += ((i + 1) * k)

if price > n:
    print(price - n)
else:
    print(0)
