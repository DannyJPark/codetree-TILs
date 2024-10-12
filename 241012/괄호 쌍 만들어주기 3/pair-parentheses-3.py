A = input()
open_count = 0
pair_count = 0

for char in A:
    if char == '(':
        open_count += 1
    elif char == ')':
        pair_count += open_count

print(pair_count)