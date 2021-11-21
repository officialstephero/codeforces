from typing import List

options = input()
options = options.split(' ')
n = options[0]
t = int(options[1])

queue = input()
queue = list(queue)

for k in range(t):
    places = []
    for i in range(0, len(queue) - 1):
        if queue[i] == 'B' and queue[i + 1] == 'G':
            places.append(queue.index('B', i))

    for i in range(len(places)):
        if places[i] != (len(queue) - 1):
            queue[places[i]] = 'G'
            queue[places[i] + 1] = 'B'

print("".join(queue))



