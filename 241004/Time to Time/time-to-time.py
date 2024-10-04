a, b, c, d = map(int, input().split())
start = a * 60 + b
end = c * 60 + d
time_diff = end - start
print(time_diff)