word = input()
upper = sum(map(str.isupper, word))

if upper > (len(word) - upper):
    print(word.upper())
else:
    print(word.lower())
