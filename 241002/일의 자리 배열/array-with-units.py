first, second = map(int, input().split())

sequence = [first, second]

for i in range(2, 10):
    next_value = (sequence[i - 2] + sequence[i - 1]) % 10 
    sequence.append(next_value)

print(" ".join(map(str, sequence)))