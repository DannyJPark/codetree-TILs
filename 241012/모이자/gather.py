n = int(input())
people = list(map(int, input().split()))
min_distance = float('inf')

for i in range(n):
    distance = 0
    for j in range(n):
        distance += abs(i - j) * people[j]
    min_distance = min(min_distance, distance)

print(min_distance)