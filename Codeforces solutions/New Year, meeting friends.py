def meeting_friends(x):
    return max(x) - min(x)


print(meeting_friends(list(map(int, input().split(' ')))))
