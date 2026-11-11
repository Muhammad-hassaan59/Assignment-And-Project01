# Name : Muhammad Hassaan
# # Trainee ID: TRN-2026-000361
# Date: 07/11/2026



#********************************************* Warm-up — — Student class ******************************

class Student:

    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
        self.marks = []

    def add_mark(self, mark):
        self.marks.append(mark)

    def average(self):
        if len(self.marks) == 0:
            return 0
        return sum(self.marks) / len(self.marks)

    def __str__(self):
        return f"{self.name} (Roll {self.rollno}): avg {self.average():.1f}"


# Create object
s1 = Student("Ali", 12)

# Add marks
s1.add_mark(80)
s1.add_mark(85)
s1.add_mark(78)

# Print student details
print(s1)

# ********************************************************************************************************
# ********************************************************************************************************

# ************************************ Build — Bank account ***********************************************


class BankAccount:

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
        self.transaction_history = []

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")

        self.balance += amount
        self.transaction_history.append(f"Deposited: {amount}")

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")

        if amount > self.balance:
            raise ValueError("Insufficient balance")

        self.balance -= amount
        self.transaction_history.append(f"Withdrawn: {amount}")

    def print_history(self):
        print("Transaction History:")

        for transaction in self.transaction_history:
            print(transaction)


# Create BankAccount object
account = BankAccount("Ali", 5000)

# Deposit money
account.deposit(2000)

# Withdraw money
account.withdraw(1000)

# Print balance
print("Owner:", account.owner)
print("Current Balance:", account.balance)

# Print transaction history
account.print_history()


# ********************************************************************************************************
# ********************************************************************************************************

#************************************* Challenge -- Library system ***************************************


class Book:
    def __init__(self, title, author, available=True):
        self.title = title
        self.author = author
        self.available = available

    def __str__(self):
        return f"{self.title} by {self.author}"


class Library:
    def __init__(self):
        self.books = []

    # Add a book
    def add_book(self, book):
        self.books.append(book)

    # Borrow a book
    def borrow(self, title):
        for book in self.books:
            if book.title == title:
                if book.available:
                    book.available = False
                    print(f"You borrowed: {title}")
                    return
                else:
                    print("Book is not available.")
                    return

        print("Book not found.")

    # Return a book
    def return_book(self, title):
        for book in self.books:
            if book.title == title:
                book.available = True
                print(f"You returned: {title}")
                return

        print("Book not found.")

    # Show available books
    def available_books(self):
        for book in self.books:
            if book.available:
                print(book)


# Inheritance
class EBook(Book):
    def __init__(self, title, author, file_size, available=True):
        super().__init__(title, author, available)
        self.file_size = file_size

    # Method overriding
    def __str__(self):
        return f"{self.title} by {self.author} ({self.file_size} MB)"


# Creating library
library = Library()

# Creating books
book1 = Book("Python Basics", "Ali")
book2 = Book("OOP Concepts", "Ahmed")
ebook1 = EBook("Learn Python", "Sara", 5)

# Adding books
library.add_book(book1)
library.add_book(book2)
library.add_book(ebook1)

# Display available books
print("Available Books:")
library.available_books()

# Borrow a book
library.borrow("Python Basics")

# Return a book
library.return_book("Python Basics")

# Display available books again
print("\nAvailable Books:")
library.available_books()

# ***************************************** The End *****************************************************

















































































































































































