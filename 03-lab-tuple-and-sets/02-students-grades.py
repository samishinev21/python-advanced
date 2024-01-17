students_num = int(input())
student_grades = {}

for _ in range(students_num):
    student_information = input().split(" ")

    name = student_information[0]
    grade = float(student_information[1])

    if name not in student_grades:
        student_grades[name] = [grade]
    else:
        student_grades[name].append(grade)

for student, grades in student_grades.items():
     avg = sum(grades) / len(grades)

     print(f"{student} -> {' '.join(map('{:.2f}'.format, grades))} (avg: {avg:.2f})")