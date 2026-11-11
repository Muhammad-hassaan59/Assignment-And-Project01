# Name : Muhammad Hassaan
# # Trainee ID: TRN-2026-000361
# Date: 07/11/2026



#********************************************* Warm-up — Standard library tour *************************************
import math
import random
import datetime
import statistics

# 1. MATH Square root of 144
result = math.sqrt(144)
print("Square root of 144:", result)


# 2. RANDOM Pick a random student
students = ["Ali", "Sara", "Ahmed", "Ayesha", "Saad"]

random_student = random.choice(students)
print("Random Student:", random_student)


# 3. DATETIME Days left until 31 December
today = datetime.date.today()

end_date = datetime.date(today.year, 12, 31)

days_left = (end_date - today).days

print("Days left until 31 December:", days_left)


# 4. STATISTICS Mean and Median of 5 marks
marks = [80, 72, 91, 95, 88]

mean = statistics.mean(marks)
median = statistics.median(marks)

print("Marks:", marks)
print("Mean:", mean)
print("Median:", median)

#*************************************************************************************************************
#*************************************************************************************************************


#************************************* Build — Your own module ********************************************

# schools_tools.py
# main.py 


#*************************************************************************************************************
#***********************************************************************************************************

#******************************************* Challenge — Real project setup **********************************************

# Create a virtual environment, install requests , save requirements.txt , and arrange this
"""folder layout:
school_app/
├── school/
│ ├── __init__.py
│ ├── grades.py
│ └── attendance.py
├── main.py
├── requirements.txt
└── .gitignore """   #I did it through Anaconda Prompt first create my venv school_env and than activate it and install requests....... u can see this in my Assignment_01  which have school_app






















































































































































