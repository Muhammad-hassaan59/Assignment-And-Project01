def make_comment(average: float) -> str:
    if average >= 90:
        return "Excellent work! Keep it up."
    elif average >= 80:
        return "Very good performance!"
    elif average >= 70:
        return "Good effort. Keep improving."
    elif average >= 50:
        return "You passed. Work harder."
    else:
        return "Needs improvement. Practice more."


def write_comment(students: list[dict]) -> None:
    rollno = int(input("Enter Student RollNo: "))

    for student in students:
        if student["RollNo"] == rollno:
            from school.student import Student

            obj = Student(
                student["Name"],
                student["RollNo"],
                student["Student_marks"]
            )

            print("Teacher Comment:", make_comment(obj.average()))
            return

    print("Student Not Found!")