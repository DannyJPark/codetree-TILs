class Student:
    def __init__(self, name, korean, english, math):
        self.name = name
        self.korean = korean
        self.english = english
        self.math = math

n = int(input())

students = []
for _ in range(n):
    name, korean, english, math = input().split()
    korean = int(korean)
    english = int(english)
    math = int(math)
    students.append(Student(name, korean, english, math))

students.sort(key=lambda student: (student.korean, student.english, student.math), reverse=True)

for student in students:
    print(f"{student.name} {student.korean} {student.english} {student.math}")