n = int(input())

home = []
guest = []

for i in range(n):
    color = list(map(int, input().split(' ')))
    home.append(color[0])
    guest.append(color[1])

k = 0
for home_color in home:
    for quest_color in guest:
        if home_color == quest_color:
            k += 1

print(k)



