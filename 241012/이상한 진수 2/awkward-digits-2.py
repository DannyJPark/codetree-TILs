a = input()
max_value = 0

for i in range(len(a)):
    modified = list(a)
    modified[i] = '1' if a[i] == '0' else '0'
    max_value = max(max_value, int("".join(modified), 2))

print(max_value)