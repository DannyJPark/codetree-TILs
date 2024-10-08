n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

events = []
for x1, x2 in segments:
    events.append((x1, 1))
    events.append((x2, -1))

events.sort()

current_overlap = 0
max_overlap = 0

for _, event in events:
    current_overlap += event
    max_overlap = max(max_overlap, current_overlap)

print(max_overlap)