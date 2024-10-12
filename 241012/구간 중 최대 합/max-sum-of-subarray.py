n, k = map(int, input().split())
numbers = list(map(int, input().split()))

max_sum = sum(numbers[:k])
current_sum = max_sum

for i in range(1, n - k + 1):
    current_sum = current_sum - numbers[i - 1] + numbers[i + k - 1]
    max_sum = max(max_sum, current_sum)

print(max_sum)