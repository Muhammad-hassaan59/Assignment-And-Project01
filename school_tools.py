
import math
import random
import datetime
import statistics


# 1. Square root
def square_root(number):
    return math.sqrt(number)


# 2. Pick a random student
def random_student(students):
    return random.choice(students)


# 3. Days left until 31 December
def days_until_december():
    today = datetime.date.today()
    end_date = datetime.date(today.year, 12, 31)

    return (end_date - today).days


# 4. Calculate mean
def calculate_mean(marks):
    return statistics.mean(marks)


# 5. Calculate median
def calculate_median(marks):
    return statistics.median(marks)


# This block runs only when school_tools.py is executed directly
if __name__ == "__main__":
    print("Testing school_tools.py")

    print("Square root:", square_root(144))

    students = ["Ali", "Sara", "Ahmed"]
    print("Random student:", random_student(students))

    print("Days left:", days_until_december())

    marks = [80, 72, 91, 95, 88]

    print("Mean:", calculate_mean(marks))
    print("Median:", calculate_median(marks))
