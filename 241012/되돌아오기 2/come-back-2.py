commands = input().strip()
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
x, y, direction_idx, time = 0, 0, 0, 0

for command in commands:
    if command == 'L':
        direction_idx = (direction_idx - 1) % 4
        time += 1
    elif command == 'R':
        direction_idx = (direction_idx + 1) % 4
        time += 1
    elif command == 'F':
        dx, dy = directions[direction_idx]
        x += dx
        y += dy
        time += 1
    
    if x == 0 and y == 0:
        print(time)
        exit()

print(-1)