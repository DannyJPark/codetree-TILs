direction_map = {
    'W': (-1, 0),  
    'S': (0, -1), 
    'N': (0, 1),   
    'E': (1, 0)  
}

N = int(input())
x, y = 0, 0 

for _ in range(N):
    direction, distance = input().split()
    distance = int(distance)
    
    dx, dy = direction_map[direction]

    x += dx * distance
    y += dy * distance

print(x, y)