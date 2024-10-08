n = int(input())
plane = [[0] * 201 for _ in range(201)]

for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1 + 100, x2 + 100):
        for j in range(y1 + 100, y2 + 100):
            plane[i][j] = 1

total_area = sum(sum(row) for row in plane)
print(total_area)