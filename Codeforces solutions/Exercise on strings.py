n = list(input().lower())

vowel = ["a", "o", "y", "e", "u", "i"]
new_n = []

for symbol in n:
    if symbol not in vowel:
        new_n.append(symbol)

for symbol in new_n:
    print(f'.{symbol}', end='')
