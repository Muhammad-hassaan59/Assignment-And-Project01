# Name:Muhammad Hassaan
# Trainee ID: TRN-2026-000361
# Date: 07/11/2026

#***************************** Warm-up — Small helpers ****************************

def area_of_circle(r):
    pi = 3.14159
    return pi * r ** 2

def is_even(n):
    return n % 2 == 0

def greet(name, lang="en"):
    greetings = {
        "en": f"Hello, {name}!",
    }
    return greetings.get(lang, greetings["en"])

print(f"Area of circle with radius 5: {area_of_circle(5)}")
print(f"Is 10 even? {is_even(10)}")
print(greet("Alice"))
print(" \n ")
print(f"Area of circle with radius 10: {area_of_circle(10)}")
print(f"Is 16 even? {is_even(16)}")
print(greet("Ali"))
print(" \n ")
print(f"Area of circle with radius 15: {area_of_circle(15)}")
print(f"Is 12 even? {is_even(12)}")
print(greet("Khan"))

#***********************************************************************************

# ************************************* Build — Marks toolkit *************************************

def average(marks):
    return sum(marks) / len(marks)


def grade(avg):
    if avg >= 80:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg >= 50:
        return "D"
    else:
        return "F"


def report(name, marks):
    avg = average(marks)
    g = grade(avg)
    return f"{name}: Average = {avg}, Grade = {g}"


# Three students
print(report("Ali", [80, 90, 85]))
print(report("Ahmed", [70, 75, 65]))
print(report("Sara", [40, 50, 45]))


# *****************************************************************************************************


# **************************************** Challenge — Comprehensions *********************************

square_numbers = [x**2 for x in range(1,11)]
print(square_numbers)   # the squares of 1–10

more_than_4letter_names = [name for name in ["Ali", "Hassan", "khan", "Umair", "Zubair"] if len(name) > 4]
print(more_than_4letter_names) #names longer than 4 letters from a lis

# a dict of {name: average} from your Part 4 result sheet; and the passing students only ( average >= 33 )

students_marks = {
    "Ali": [80, 72, 91],
    "Sara": [95, 88, 90],
    "Ahmed": [70, 75, 80],
    "Ayesha": [37, 90, 92],
    "Saad": [39, 95, 70]
}

def average():
    avg = {}
    for name, marks in students_marks.items():
        avg[name] = sum(marks) / len(marks)
    return avg


student_with_average = average()
print(student_with_average)


#************************************** The End ************************************************************
