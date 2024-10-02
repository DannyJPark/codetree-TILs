n = int(input())
grades = list(map(float, input().split()))
average = sum(grades) / n
print(f"{average:.1f}")
if average >= 4.0:
    print("Perfect")
elif average >= 3.0:
    print("Good")
else:
    print("Poor")