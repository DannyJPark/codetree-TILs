N = int(input())
numbers = list(map(int, input().split()))
count = 0

for i in range(N):
    for j in range(i, N):
        subarray = numbers[i:j+1]
        avg = sum(subarray) / len(subarray)
        if avg in subarray:
            count += 1

print(count)