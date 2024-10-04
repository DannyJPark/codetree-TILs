n = int(input())
numbers = list(map(int, input().split()))
numbers.sort()
max_group_sum = 0
for i in range(n):
    group_sum = numbers[i] + numbers[2 * n - 1 - i]
    max_group_sum = max(max_group_sum, group_sum)
print(max_group_sum)