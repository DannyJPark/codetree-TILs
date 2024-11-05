n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
r, c = map(int, input().split())
r -= 1
c -= 1

radius = grid[r][c]
for i in range(-radius + 1, radius):
    nx, ny = r + i, c
    if 0 <= nx < n:
        grid[nx][ny] = 0
    nx, ny = r, c + i
    if 0 <= ny < n:
        grid[nx][ny] = 0

for j in range(n):
    empty_spots = [0] * n
    fill_index = n - 1
    for i in range(n - 1, -1, -1):
        if grid[i][j] != 0:
            empty_spots[fill_index] = grid[i][j]
            fill_index -= 1
    for i in range(n):
        grid[i][j] = empty_spots[i]

for row in grid:
    print(" ".join(map(str, row)))