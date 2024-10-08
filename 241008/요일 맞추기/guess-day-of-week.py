days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
weekdays = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

m1, d1, m2, d2 = map(int, input().split())

if m1 == m2:
    day_diff = d2 - d1
else:
    day_diff = days_in_month[m1 - 1] - d1
    for month in range(m1 + 1, m2):
        day_diff += days_in_month[month - 1]
    day_diff += d2

weekday_index = (day_diff % 7) % 7
print(weekdays[weekday_index])