numbers = list(map(int, input().split()))

zero_index = numbers.index(0)

if zero_index >= 3:
    last_three_sum = sum(numbers[zero_index-3:zero_index])
else:
    last_three_sum = sum(numbers[:zero_index])

print(last_three_sum)