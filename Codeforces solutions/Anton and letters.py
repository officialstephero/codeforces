n = input()

if len(n) == 2:
    print(0)
else:
    n = n[1:-1].split(', ')
    fil = []

    for letter in n:
        if letter not in fil:
            fil.append(letter)

    print(len(fil))
