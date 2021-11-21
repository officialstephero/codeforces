n = int(input())
percent = input().split(' ')
percent = [int(i) for i in percent]
print('{:.12f}'.format(sum(percent) / n))
