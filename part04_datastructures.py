# Name : Muhammad Hassaan
# Trainee ID : TRN-2026-000361
# Date : 05/11/2026

# ************************* Warm-up — Shopping list *********************************

items = ["milk", "bread", "eggs"]

items.append("tea")

items.remove("bread")

items.sort()

for index, item in enumerate(items):
    print(f"{index}. {item}")


#******************************************************************************************

#************************************* Build — Phone book ***********************************

contacts = {"Ali":33345678765, "Sara": 23456787654, "Ahmed": 3456787654,
            "Ayesha": 35678909876, "Saad": 45678909876}

while True:
    print("Phone Book Menu: ")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Delete Contact")
    print("4. Display All Contacts")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        name = input("Enter contact name: ")
        number = input("Enter contact number: ")
        contacts[name] = number
        print(f"Contact {name} added successfully.")

    elif choice == "2":
        name = input("Enter contact name to search: ")
        if name in contacts:
            print(f"{name}: {contacts[name]}")
        else:
            print(f"Contact {name} not found.")
    elif choice == "3":
        name = input("Enter contact name to delete: ")
        if name in contacts:
            del contacts[name]
            print(f"Contact {name} deleted successfully.")
        else:
            print(f"Contact {name} not found.")
    elif choice == "4":
        print("All Contacts:")
        for name, number in contacts.items():
            print(f"{name}: {number}")
    elif choice == "5":
        print("Exiting Phone Book. Goodbye!")
        break

#******************************************************************************************

#*****************************Challenge — Class result sheet *******************************

students_marks = {
    "Ali": [80, 72, 91],
    "Sara": [95, 88, 90],
    "Ahmed": [70, 75, 80],
    "Ayesha": [37, 90, 92],
    "Saad": [39, 95, 70]
}


toppers = set()
failed_subject_students = set()


for student, marks in students_marks.items():
    total = sum(marks)
    average = total / len(marks)

    print("\nStudent:", student)
    print("Marks:", marks)
    print("Total Marks:", total)
    print("Average Marks:", average)

    
    if average >= 80:
        toppers.add(student)

    
    if any(mark < 40 for mark in marks):
        failed_subject_students.add(student)



print("\nToppers:", toppers)
print("Failed Subject Students:", failed_subject_students)

# ************************************* The End *************************************






        




































































