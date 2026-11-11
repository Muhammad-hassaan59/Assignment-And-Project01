# Name : Muhammad Hassaan
# Trainee ID : TRN-2026-000361
# Date : 05/11/2026

# ***************** Warm-up — Print table *******************************

value = int(input("Enter a number to print its multiplication table: "))

i = 1

while i <= 10:
    result = value * i
    print(f"{value} x {i} = {result}")
    i += 1

# *****************************Build — ATM PIN check*******************************


pin = int(input("Enter your 4-digit PIN: "))
correct_pin = 4321
tries = 3
iteration = 0

while iteration < tries:
    if pin == correct_pin:
        print("Access granted. Welcome!")
        break
    else:
        iteration += 1
        if iteration < tries:
            print(f"Incorrect PIN. You have {tries - iteration} attempts left.")
            pin = int(input("Please try again: "))
        else:
            print("Access denied. Too many incorrect attempts.")


  # ***********************************************************************************  


# ************************ Challenge — Number guessing game ****************************

import random as rd  # importing random module to generate random numbers (as rd means random)

gussing_number = rd.randint(1, 50)  

iteration = 0

while True:
    iteration += 1
    user_guess = int(input("Guess a number between 1 and 50: "))

    if gussing_number == user_guess:
        print(f"Got it in {iteration} guesses!")
        ask = input("Do you want to play again? (yes/no): ").lower()

        if ask == "yes":
            gussing_number = rd.randint(1, 50) 
            iteration = 0  
            continue    
        else:
            print("Thanks for playing!")
        break

    elif gussing_number > user_guess:
        print("Too low! Try again.")

    elif gussing_number < user_guess:
        print("Too high! Try again.")   

# #*******************************The End *****************************************
    
     





























