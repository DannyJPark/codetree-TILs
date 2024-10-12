n, m = map(int, input().split())
grid = [[0] * m for _ in range(n)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

x, y, dir_idx = 0, 0, 0
num = 1

while num <= n * m:
    grid[x][y] = num
    num += 1
    nx, ny = x + dx[dir_idx], y + dy[dir_idx]
    
    if nx < 0 or nx >= n or ny < 0 or ny >= m or grid[nx][ny] != 0:
        dir_idx = (dir_idx + 1) % 4
        nx, ny = x + dx[dir_idx], y + dy[dir_idx]
    
    x, y = nx, ny

for row in grid:
    print(*row)