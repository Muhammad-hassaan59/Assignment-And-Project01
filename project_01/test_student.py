
from school.student import Student


def test_student_creation():
    student = Student("Aiman", 4)
    assert student.name == "Aiman"
    assert student.rollno == 4


def test_add_marks():
    student = Student("Aiman", 4)
    student.student_marks.append(80)
    student.student_marks.append(90)

    assert student.student_marks == [80, 90]


def test_average():
    student = Student("Aiman", 4, [80, 90, 70])
    assert student.average() == 80.0


def test_grade():
    student = Student("Aiman", 4, [90, 95, 85])
    assert student.grade() == "A+"


def test_empty_marks():
    student = Student("Aiman", 4)
    assert student.average() == 0.0
    assert student.grade() == "N/A"


def test_student_string():
    student = Student("Ali", 12, [80, 82])
    assert str(student) == "Ali (Roll 12): avg 81.0"


def test_into_dict():
    student = Student("Aiman", 4, [80, 90])
    expected = {
        "Name": "Aiman",
        "RollNo": 4,
        "Student_marks": [80, 90]
    }

    assert student.into_dict() == expected
