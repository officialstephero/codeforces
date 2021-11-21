horseshoes = input().split(' ')
new_hors = []

for i in range(len(horseshoes)):
    if horseshoes[i] not in new_hors:
        new_hors.append(horseshoes[i])

print(4 - len(new_hors))
