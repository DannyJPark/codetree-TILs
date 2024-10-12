N = int(input())
people = [tuple(input().split()) for _ in range(N)]
people = [(int(pos), flag) for pos, flag in people]
people.sort()

max_size = 0

for i in range(N):
    g_count = 0
    h_count = 0
    for j in range(i, N):
        if people[j][1] == 'G':
            g_count += 1
        elif people[j][1] == 'H':
            h_count += 1
        
        if g_count == 0 or h_count == 0 or g_count == h_count:
            max_size = max(max_size, people[j][0] - people[i][0])

print(max_size)