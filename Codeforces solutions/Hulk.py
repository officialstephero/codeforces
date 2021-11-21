import math

n = int(input())
hate = "I hate that"
love = "I love that"
it = "it"
answer = []

for i in range(1, n + 1):
    if math.fmod(i, 2) == 0:
        answer += love
    else:
        answer += hate
    answer.append(" ")

answer = answer[0:-5] + list(it)
print("".join(answer))
