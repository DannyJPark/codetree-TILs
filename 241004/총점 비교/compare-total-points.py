class Student:
    def __init__(self, name, korean, english, math):
        self.name = name
        self.korean = korean
        self.english = english
        self.math = math
        self.total_score = korean + english + math 

n = int(input("학생 수를 입력하세요: "))

students = []
for _ in range(n):
    name, korean, english, math = input().split()
    korean = int(korean)
    english = int(english)
    math = int(math)
    students.append(Student(name, korean, english, math))

students.sort(key=lambda student: student.total_score)
for student in students:
    print(f"{student.name} {student.korean} {student.english} {student.math}")