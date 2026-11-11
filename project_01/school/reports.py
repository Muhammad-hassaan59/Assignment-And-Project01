from school.student import Student

from school.student import Student


# ============== SHOW REPORT CARD ==============

def show_report_card(students: list[dict]) -> None:

    rollno = int(input("Enter Student RollNo: "))

    for s in students:

        if s["RollNo"] == rollno:

            student = Student(
                s["Name"],
                s["RollNo"],
                s["Student_marks"]
            )

            print("\n===== REPORT CARD =====")
            print("Name:", student.name)
            print("Roll Number:", student.rollno)
            print("Marks:", student.student_marks)
            print("Average:", student.average())
            print("Grade:", student.grade())

            return

    print("Student Not Found!")


# ============== CLASS RANKING ==============

def class_ranking(students: list[dict]) -> None:

    if not students:
        print("No students found!")
        return

    student_objects = []

    for s in students:

        student = Student(
            s["Name"],
            s["RollNo"],
            s["Student_marks"]
        )

        student_objects.append(student)

    ranking = sorted(
        student_objects,
        key=lambda student: student.average(),
        reverse=True
    )

    print("\n===== CLASS RANKING =====")

    for position, student in enumerate(ranking, start=1):

        print(
            position,
            student.name,
            "| RollNo:", student.rollno,
            "| Average:", student.average()
        )
