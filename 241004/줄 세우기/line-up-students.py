class Student:
    def __init__(self, height, weight, number):
        self.height = height
        self.weight = weight
        self.number = number

n = int(input())

students = []
for i in range(n):
    height, weight = map(int, input().split())
    students.append(Student(height, weight, i + 1))  
students.sort(key=lambda student: (-student.height, -student.weight, student.number))

for student in students:
    print(f"{student.height} {student.weight} {student.number}")