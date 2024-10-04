n = int(input())
sequence = list(map(int, input().split()))

indexed_sequence = [(value, index) for index, value in enumerate(sequence)]

indexed_sequence.sort(key=lambda x: x[0])

result = [0] * n

for new_index, (value, original_index) in enumerate(indexed_sequence):
    result[original_index] = new_index + 1 
print(" ".join(map(str, result)))