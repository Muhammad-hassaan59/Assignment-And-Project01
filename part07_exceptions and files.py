# Name : Muhammad Hassaan
# # Trainee ID: TRN-2026-000361
# Date: 07/11/2026



#********************************************* Warm-up — Safe division *************************************


while True:  
    try:
        first_number = int(input("Enter First Number: "))
        second_number = int(input("Enter Second Number: "))

        result = first_number / second_number

        print("Result:", result)
        break

    except ValueError:
        print("Not a number!")

    except ZeroDivisionError:
        print("Error! You cannot divide by zero. Try again.")


#********************************************************************************************************
#********************************************************************************************************



#********************************************** Build — Daily diary **********************************************************

import datetime  # Best practice is that if some thing you wanna import so import it in the beginning of the file

while True:
    print("\n===== MY DAILY DIARY =====")
    print("1. Add Today's Note")
    print("2. View All Entries")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        today = datetime.date.today()

        note = input("Write your today's note: ")

        with open("diary.txt", "a") as file:
            file.write(f"\nDate: {today}\n")
            file.write(f"Note: {note}\n")
            file.write("--------------------\n")

        print("Your note has been saved!")

    elif choice == "2":
        try:
            with open("diary.txt", "r") as file:
                content = file.read()

                if content.strip(): # removes extra spaces and newline characters from the beginning and end of a string
                    print("\n===== PAST DIARY ENTRIES =====")
                    print(content)
                else:
                    print("No entries yet")

        except FileNotFoundError:
            print("No entries yet")

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice! Please try again.")


#********************************************************************************************************
#********************************************************************************************************

#***************************************** Challenge — CSV result sheet ***************************************************************

import csv
import json

students_marks = {
    "Ali": [80, 72, 91],
    "Sara": [95, 88, 90],
    "Ahmed": [70, 75, 80],
    "Ayesha": [37, 90, 92],
    "Saad": [39, 95, 70]
}

# Prepare result sheet
results = []

for student, marks in students_marks.items():

    average = sum(marks) / len(marks)

    results.append({
        "name": student,
        "mark1": marks[0],
        "mark2": marks[1],
        "mark3": marks[2],
        "average": average
    })


# Save data in CSV
with open("results.csv", "w", newline="") as file:

    writer = csv.DictWriter(
        file,
        fieldnames=["name", "mark1", "mark2", "mark3", "average"]
    )

    writer.writeheader()
    writer.writerows(results)

print("CSV file saved successfully!")


# Save data in JSON
with open("results.json", "w") as file:

    json.dump(results, file, indent=4)

print("JSON file saved successfully!")

# PART 2 Second program — Read CSV and find topper


with open("results.csv", "r") as file:

    reader = csv.DictReader(file)

    topper = None

    for student in reader:

        average = float(student["average"])

        if topper is None or average > float(topper["average"]):
            topper = student


print("===== CLASS TOPPER =====")

print("Name:", topper["name"])
print("Marks:",
      topper["mark1"],
      topper["mark2"],
      topper["mark3"])

print("Average:", topper["average"])

# **************************************** The End *********************************************************