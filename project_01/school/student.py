from dataclasses import dataclass, field


@dataclass
class Student:
    name: str
    rollno: int
    student_marks: list[int] = field(default_factory=list)

    def into_dict(self) -> dict:
        return {
            "Name": self.name,
            "RollNo": self.rollno,
            "Student_marks": self.student_marks
        }

    def average(self) -> float:
        if not self.student_marks:
            return 0.0

        return sum(self.student_marks) / len(self.student_marks)

    def grade(self) -> str:
        avg = self.average()

        if not self.student_marks:
            return "N/A"
        elif avg >= 90:
            return "A+"
        elif avg >= 80:
            return "A"
        elif avg >= 70:
            return "B"
        elif avg >= 60:
            return "C"
        elif avg >= 50:
            return "D"
        else:
            return "F"

    def __str__(self) -> str:
        return f"{self.name} (Roll {self.rollno}): avg {self.average():.1f}"