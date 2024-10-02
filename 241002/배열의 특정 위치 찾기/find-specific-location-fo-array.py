numbers = list(map(int, input().split()))

even_index_sum = sum(numbers[i] for i in range(1, 10, 2))

multiple_of_three_values = [numbers[i] for i in range(2, 10, 3)]

if multiple_of_three_values:
    multiple_of_three_avg = sum(multiple_of_three_values) / len(multiple_of_three_values)
else:
    multiple_of_three_avg = 0

print(f"{even_index_sum} {multiple_of_three_avg:.1f}")