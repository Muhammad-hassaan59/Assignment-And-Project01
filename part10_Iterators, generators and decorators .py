# Name : Muhammad Hassaan
# # Trainee ID: TRN-2026-000361
# Date: 08/11/2026



#******************************************** Warm-up — Countdown generator ******************************


# Countdown generator
def countdown(n):
    while n > 0:
        yield n
        n -= 1


# Loop over countdown
for number in countdown(5):
    print(number)


# Even numbers generator
def evens(limit):
    for num in range(0, limit + 1, 2):
        yield num


# Print even numbers as a list
print(list(evens(10)))


# *********************************************************************************************************
# *********************************************************************************************************

# ************************************* Build — Big file reader *****************************************************


#Creating a text file with 50 lines
with open("log.txt", "w") as file:
    for i in range(1, 51):
        if i % 5 == 0:
            file.write(f"Line {i}: ERROR something went wrong\n")
        else:
            file.write(f"Line {i}: Program running successfully\n")


# Generator to read file line by line
def read_lines(path):
    with open(path, "r") as file:
        for line in file:
            yield line


# Generator to return only ERROR lines
def only_errors(lines):
    for line in lines:
        if "ERROR" in line:
            yield line


# Count ERROR lines without creating a list
count = 0

for line in only_errors(read_lines("log.txt")):
    print(line.strip())
    count += 1

print("Total ERROR lines:", count)


# *********************************************************************************************************
# *********************************************************************************************************




import time
from functools import wraps


# Timer decorator
def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()

        result = func(*args, **kwargs)

        end = time.time()
        print(f"Time taken: {end - start:.6f} seconds")

        return result

    return wrapper


# Log calls decorator
def log_calls(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Function name: {func.__name__}")
        print(f"Arguments: {args}")
        print(f"Keyword arguments: {kwargs}")

        result = func(*args, **kwargs)

        return result

    return wrapper


# Applying both decorators
@timer
@log_calls
def calculate_sum(n):
    total = 0

    for i in range(1, n + 1):
        total += i

    return total


# Function call
answer = calculate_sum(1000000)

print("Sum:", answer)




# ****************************************     THE END        *****************************************************************
# *********************************************************************************************************





































































































































































































