N, K = map(int, input().split())
people = [tuple(input().split()) for _ in range(N)]
people = [(int(pos), flag) for pos, flag in people]
people.sort()

max_score = 0

for i in range(N):
    score = 0
    for j in range(i, N):
        if people[j][0] - people[i][0] > K:
            break
        if people[j][1] == 'G':
            score += 1
        elif people[j][1] == 'H':
            score += 2
    max_score = max(max_score, score)

print(max_score)