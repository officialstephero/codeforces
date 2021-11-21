n = int(input())
points = input().split()
if points.count('0') != len(points):
    print('HARD')
else:
    print('EASY')
