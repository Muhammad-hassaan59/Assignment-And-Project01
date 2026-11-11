# Name = Muhammad Hassaan
# Trainee ID = TRN-2026-000361
# Date = 05/11/2026

# ***************** Warm-up — Even, odd and sign ****************************************

number = int(input("Enter a number:"))

if number > 0:
    print(f"{number} is a positive number.")
    if number %2 == 0:
        print(f"{number} is an even number.")

    else:
        print(f"{number} is an odd number.")

elif number < 0:
    print(f"{number} is a negative number.")
    if number %2 == 0:
        print(f"{number} is an even number.")
    
    else:
        print(f"{number} is an odd number.")

else:
    print(f"{number} is zero.")


 # *************************************************************************************   


#  ***************** Build — Grade Calculator ****************************************

marks = int(input("Enter marks: "))

if marks < 0 or marks > 100:
    print("Invalid marks.")
elif marks >= 80:
    print("Grade: A")
elif marks >= 70:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
elif marks >= 33:
    print("Grade: D")
else:
    print("Grade: Fail")

# ****************************************************************************************

# **************************** Challenge — Electricity bill ******************************

units = int(input("Enter the number of units consumed: "))

if units < 0:
    print("Invalid input. Please enter a valid number of units.")

else:
    if units <= 100:
        bill = units * 10
    elif units <= 200:
        bill = (100 * 10) + ((units - 100) * 15)
    else:
        bill = (100 * 10) + (100 * 15) + ((units - 200) * 20)

    bill += 50
    print(f"Total electricity bill (including fixed charges of 50 Rs): {bill} Rs")


    # ***************************************The End****************************************