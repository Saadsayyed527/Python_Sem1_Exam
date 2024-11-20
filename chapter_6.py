# chapter 6 

# 6.1 Exception Handling
# Exception handling is a mechanism to handle errors or exceptions that may occur during the execution of a program. Python provides the try, except, finally, and raise constructs for handling exceptions.

# Key Concepts and Syntax
# try and except:

# Code that may throw an exception is placed inside the try block.
# If an exception occurs, it is caught in the except block.

try:
    x = int(input("Enter a number: "))
    result = 10 / x
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed!")
except ValueError:
    print("Error: Invalid input. Please enter a number.")


# finally:

# The finally block is executed no matter what happens in the try block. It is used for cleanup actions.

try:
    file = open("example.txt", "r")
    content = file.read()
    print(content)
except FileNotFoundError:
    print("Error: File not found.")
finally:
    file.close()
    print("File closed.")



# raise:

# The raise statement allows you to manually throw an exception

def check_age(age):
    if age < 18:
        raise ValueError("Age must be at least 18.")
    return "Access granted."

try:
    print(check_age(16))
except ValueError as e:
    print("Exception caught:", e)

# ----------------------------------------

# 6.2 Multithreading and 
# 6.3. Synchronizing the threads: sleep(), join()


# Multithreading allows a program to run multiple threads concurrently, improving efficiency for I/O-bound tasks. Each thread operates as a separate flow of execution.

# Creating Threads
# Using the threading Module:

# Threads can be created using the threading module

from threading import *
from time import sleep

class Hello(Thread): # creating threads
    def run(self):  # run class is already in the threading class 
        for i in range(5):
            print("hello")
            sleep(1)

class Hi(Thread):
    def run(self):
        for i in range(5):
            print("Hi")
            sleep(1)

t1 = Hello()
t2 = Hi()

t1.start()   # while start method called it will automatically call the run method 
sleep(0.2)
t2.start()

t1.join()  # join method is used when we have to complete all the threads work  or else it will directly  print byy 
t2.join()
print("byy")
