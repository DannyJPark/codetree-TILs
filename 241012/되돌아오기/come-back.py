N = int(input())
directions = {'N': (0, 1), 'S': (0, -1), 'E': (1, 0), 'W': (-1, 0)}

x, y = 0, 0
time = 0

for _ in range(N):
    direction, distance = input().split()
    distance = int(distance)
    dx, dy = directions[direction]
    
    for _ in range(distance):
        x += dx
        y += dy
        time += 1
        
        if x == 0 and y == 0:
            print(time)
            exit()

print(-1)