n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
count = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n):
    for j in range(n):
        adjacent_ones = 0
        for d in range(4):
            ni, nj = i + dx[d], j + dy[d]
            if 0 <= ni < n and 0 <= nj < n:
                if grid[ni][nj] == 1:
                    adjacent_ones += 1
        if adjacent_ones >= 3:
            count += 1

print(count)