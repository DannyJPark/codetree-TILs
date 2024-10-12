n = int(input())
grid = [input().strip() for _ in range(n)]
k = int(input())

# 시작 위치 설정
if 1 <= k <= n:
    x, y, direction = 0, k - 1, 2
elif n < k <= 2 * n:
    x, y, direction = k - n - 1, n - 1, 3
elif 2 * n < k <= 3 * n:
    x, y, direction = n - 1, 3 * n - k, 0
else:
    x, y, direction = 4 * n - k, 0, 1

# 방향 설정 (상, 우, 하, 좌)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 거울에 의한 방향 변화 설정
def reflect(mirror, direction):
    if mirror == '/':
        if direction == 0: return 1
        elif direction == 1: return 0
        elif direction == 2: return 3
        elif direction == 3: return 2
    elif mirror == '\\':
        if direction == 0: return 3
        elif direction == 1: return 2
        elif direction == 2: return 1
        elif direction == 3: return 0

# 레이저 경로 탐색
bounce_count = 0

while 0 <= x < n and 0 <= y < n:
    mirror = grid[x][y]
    direction = reflect(mirror, direction)
    bounce_count += 1
    x += dx[direction]
    y += dy[direction]

print(bounce_count)