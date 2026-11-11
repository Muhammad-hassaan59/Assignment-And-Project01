#
# Name = Muhammad Hassaan
# Trainee ID = TRN-2026-000361
# Date = 10/11/2026

# ================= IMPORTS =================

from school.student import Student
from school.reports import show_report_card, class_ranking
from school.comments import write_comment

import os
import json
import logging


# ================= LOGGING =================

logging.basicConfig(
    filename="school.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


# ================= FILE FUNCTIONS =================

def load_students() -> list[dict]:
    if not os.path.exists("school.json"):
        return []

    with open("school.json", "r") as file:
        data = json.load(file)

    if not isinstance(data, list):
        raise ValueError("Invalid school data format.")

    return data


def save_students(students: list[dict]) -> None:
    with open("school.json", "w") as file:
        json.dump(students, file, indent=4)

    logging.info("Student data saved successfully.")


# ================= MAIN PROGRAM =================

def main() -> None:

    while True:

        print("\n===== SCHOOL MANAGEMENT =====")
        print("1. ADD STUDENT")
        print("2. ADD MARKS")
        print("3. SHOW REPORT CARD")
        print("4. CLASS RANKING")
        print("5. WRITE COMMENT")
        print("6. SAVE AND EXIT")

        choice = input("Enter your choice: ")

        try:

            # ============== ADD STUDENT ==============

            if choice == "1":

                name = input("Enter Student Name: ")

                if not name.strip():
                    raise ValueError("Name cannot be empty!")

                rollno = int(input("Enter RollNo: "))

                if rollno <= 0:
                    raise ValueError("Roll number must be positive!")

                students = load_students()

                if any(s["RollNo"] == rollno for s in students):
                    print("Student already exists!")

                else:
                    student = Student(name, rollno)

                    students.append(student.into_dict())

                    save_students(students)

                    logging.info(
                        "Student added: %s, RollNo: %s",
                        name, rollno
                    )

                    print("Student added successfully!")

            # ============== ADD MARKS ==============

            elif choice == "2":

                rollno = int(input("Enter Student RollNo: "))

                students = load_students()
                found = False

                for s in students:

                    if s["RollNo"] == rollno:

                        print("Student Found:", s["Name"])

                        subjects_marks = input(
                            "Enter 6 Subject Marks separated by commas: "
                        )

                        new_marks = [
                            int(mark.strip())
                            for mark in subjects_marks.split(",")
                        ]

                        if len(new_marks) != 6:
                            raise ValueError("Enter exactly 6 marks!")

                        if not all(0 <= mark <= 100 for mark in new_marks):
                            raise ValueError(
                                "Marks must be between 0 and 100!"
                            )

                        s["Student_marks"] = new_marks

                        found = True
                        break

                if found:

                    save_students(students)

                    logging.info(
                        "Marks updated for RollNo: %s", rollno
                    )

                    print("Marks updated successfully!")

                else:
                    print("Student Not Found!")

            # ============== REPORT CARD ==============

            elif choice == "3":

                students = load_students()
                show_report_card(students)

            # ============== CLASS RANKING ==============

            elif choice == "4":

                students = load_students()
                class_ranking(students)

            # ============== TEACHER COMMENT ==============

            elif choice == "5":

                students = load_students()
                write_comment(students)

            # ============== SAVE AND EXIT ==============

            elif choice == "6":

                students = load_students()
                save_students(students)

                print("Data saved successfully!")
                logging.info("School Manager closed.")

                print("Goodbye!")
                break

            else:
                print("Invalid choice! Please select 1-6.")

        except ValueError as e:
            print("Input Error:", e)
            logging.error("Input error: %s", e)

        except (OSError, json.JSONDecodeError, KeyError, TypeError) as e:
            print("File or data error:", e)
            logging.exception("File or data operation failed")


# ================= PROGRAM START =================

if __name__ == "__main__":
    main()




















































































































































































































































































































