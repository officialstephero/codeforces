print(*[(lambda x: x[2] - (x[2] - x[1]) % x[0])(list(map(int, input().split()))) for _ in range(int(input()))], sep='\n')

