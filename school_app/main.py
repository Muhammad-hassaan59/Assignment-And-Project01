from school.grades import calculate_grade
from school.attendance import attendance_percentage

marks = 85

grade = calculate_grade(marks)

attendance = attendance_percentage(18, 20)

print("Grade:", grade)
print("Attendance:", attendance, "%")