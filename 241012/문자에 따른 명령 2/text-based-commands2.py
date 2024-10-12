directions = ['N', 'E', 'S', 'W']

dx_dy = {
    'N': (0, 1),  
    'E': (1, 0),  
    'S': (0, -1),  
    'W': (-1, 0)   
}
commands = input().strip()
x, y = 0, 0
current_direction = 0 

for command in commands:
    if command == 'L':  
        current_direction = (current_direction - 1) % 4
    elif command == 'R':  
        current_direction = (current_direction + 1) % 4
    elif command == 'F':  
        dx, dy = dx_dy[directions[current_direction]]
        x += dx
        y += dy
print(x, y)