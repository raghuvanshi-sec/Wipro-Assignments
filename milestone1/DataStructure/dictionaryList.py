students = {}

n = int(input("Enter number of students: "))

for i in range(n):
    name = input("Enter student name: ")
    math = float(input("Math marks: "))
    physics = float(input("Physics marks: "))
    chemistry = float(input("Chemistry marks: "))
    students[name] = [math, physics, chemistry]

search = input("Enter student name to find average: ")

if search in students:
    marks = students[search]
    average = sum(marks) / len(marks)
    print("Average percentage marks:", average)
else:
    print("Student not found")