days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

m1, d1, m2, d2 = map(int, input().split())

if m1 == m2:
    result = d2 - d1 + 1
else:
   
    result = days_in_month[m1 - 1] - d1 + 1

    for month in range(m1 + 1, m2):
        result += days_in_month[month - 1]

    result += d2

print(result)