import math

nicks = str(input())
nicks = list(nicks)
unique = []

for nick in nicks:
    if nick not in unique:
        unique.append(nick)

if math.fmod(len(unique), 2) != 0:
    print('IGNORE HIM!')
else:
    print('CHAT WITH HER!')
