n = int(input())
words = []
for i in range(n):
    word = str(input())
    words.append(word)

for i in range(n):
    if len(words[i]) > 10:
        word = words[i]
        print(word[0] + str(len(word) - 2) + word[-1])
    else:
        word = words[i]
        print(word)
