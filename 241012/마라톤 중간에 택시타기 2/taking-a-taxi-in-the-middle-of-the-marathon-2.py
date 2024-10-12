N = int(input())
points = [tuple(map(int, input().split())) for _ in range(N)]

def distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

total_distance = sum(distance(points[i], points[i+1]) for i in range(N-1))
min_distance = total_distance

for i in range(1, N-1):
    skipped_distance = total_distance - distance(points[i-1], points[i]) - distance(points[i], points[i+1]) + distance(points[i-1], points[i+1])
    min_distance = min(min_distance, skipped_distance)

print(min_distance)