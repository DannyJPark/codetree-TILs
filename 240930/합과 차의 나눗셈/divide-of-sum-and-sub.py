a, b = map(int, input().split())
sum1 = a + b
diff = a - b
result = round(sum1 / diff, 2)
print(f'{result:.2f}')