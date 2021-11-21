n = int(input())
win_rate = list(input())

if win_rate.count('A') > win_rate.count('D'):
    print('Anton')
elif win_rate.count('A') < win_rate.count('D'):
    print('Danik')
else:
    print('Friendship')
