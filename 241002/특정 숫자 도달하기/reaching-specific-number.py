numbers = list(map(int, input().split()))


count = 0
limit_index = 10 

for i in range(10):
    if numbers[i] >= 250:
        limit_index = i
        break


sum_numbers = sum(numbers[:limit_index])
count = limit_index


if count == 0:
    sum_numbers = sum(numbers)
    count = 10


average = sum_numbers / count

print(sum_numbers, average)