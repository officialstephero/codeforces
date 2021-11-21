print(*[(max(max(ab), 2 * min(ab)))**2 for ab in (list(map(int, input().split())) for _ in range(int(input())))], sep='\n')
