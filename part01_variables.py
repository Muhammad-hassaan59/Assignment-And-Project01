# Name = Muhammad Hassaan
# Trainee ID = TRN-2026-000361
# Date = 05/11/2026

# **************** Warmpup Exercise ****************

Name = input("What is your name? ")
Age = int(input("How old are you? "))
Class = input("What class are you in? ")
City = input("What city do you live in? ")

print(f"======== STUDENT CARD ========")

print(f"{Name} And Type is {type(Name)}")
print(f"{Age} And Type is {type(Age)}")
print(f"{Class} And Type is {type(Class)}")
print(f"{City} And Type is {type(City)}")

print("================================")


# ************************* BUILD -- SHOP BILL *************************

product_name = input("Enter the product name: ")
price = float(input("Enter the price of the product: "))
quantity = int(input("Enter the quantity of the product: "))

subtotal = price * quantity
print(f"Subtotal: {subtotal}")

five_percent_discount = subtotal * 0.05
print(f"5% Discount: {five_percent_discount}")

seventeen_percent_tax_discount_amount= five_percent_discount * 0.17
print(f"17% Tax Discount Amount: {seventeen_percent_tax_discount_amount}")

final_amount = subtotal - five_percent_discount + seventeen_percent_tax_discount_amount
print(f"Final Amount: {round(final_amount, 2)}")

# *****************************************************************************



# ************************* CHALLENGE — UNIT CONVERTER *************************

temperature_celsius = float(input("Enter the temperature in Celsius: "))
distance_kilometers = float(input("Enter the distance in kilometers: "))
celcius_to_fahrenheit = (temperature_celsius * 9/5) + 32
kilometers_to_miles = distance_kilometers * 0.621371
celcius_to_kelvin = temperature_celsius + 273.15

print(f"Temperature in Fahrenheit: {round(celcius_to_fahrenheit,1)}")
print(f"Distance in Miles: {round(kilometers_to_miles,1)}")
print(f"Temperature in Kelvin: {round(celcius_to_kelvin,1)}")


# ******************************************* The End *******************************************