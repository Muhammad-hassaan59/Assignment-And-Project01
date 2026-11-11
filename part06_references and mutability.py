# Name : Muhammad Hassaan
# # Trainee ID: TRN-2026-000361
# Date: 07/11/2026

import copy # It is library module

#********************************************* Warm-up — Predict, then run ******************************

a = [1, 2, 3]
b = a
b.append(4)
print(a) # Pridiction were clear that value will be appended to a 



c = a.copy()
c.append(5)
print(a, c) # I am not surprise because c is the copy of a we can make changes in it and it did't reflect in original list if we make changes in it copy list
print(a is b, a is c, a == a[:])


# ***********************************************************************************************************************************

# ******************************************* Build — Fix the cart bug *******************************************************************


def add_item(item, cart=[]):
    cart.append(item)
    return cart

print(add_item("Apple"))
print(add_item("Bannana"))  # Item is adding in the same cart


def add_items(item, cart=None): # Fxing the error through None why None if cart is equal to None (cart = None or cart is none) than it will create new list
    if cart is None:            
        cart = []

    cart.append(item)
    return cart


print(add_items("Apple"))
print(add_items("Bannana"))

# **************************************************************************************************************************************************



# ******************************************* Challenge — Safe class copy **********************************


classes = {"A": ["Ali", "Sara"]}

# Shallow Copy
first_class = copy.copy(classes)
first_class["A"].append("Zaid")     # Shallow copy can affect the original list of students

# Deep Copy
second_class = copy.deepcopy(classes)
second_class["A"].append("Haris") # Deep copy creat a completely independent copy 

print(f"This Is Shallow Copy: {first_class}")
print(f"This Is Deep Copy: {second_class}")
print(f"This Is Original: {classes}") # Zaid is added to original list of dict

# ******************************************** The End ***************************************************************











