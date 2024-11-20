# chapter 3 

# 3.1 Function Basics
# A function is a reusable block of code designed to perform a specific task.

# Scope:

# Local Scope: Variables declared inside a function are local to that function.

# Global Scope: Variables declared outside any function are accessible globally unless shadowed.

# Non-Local Scope: Variables in enclosing functions, accessed using nonlocal.

x = 10  # Global variable

def outer_function():
    x = 5  # Local to outer_function

    def inner_function():
        nonlocal x  # Refers to x in the outer_function scope
        x += 1
        print("Inner:", x)  # Output: Inner: 6

    inner_function()
    print("Outer:", x)  # Output: Outer: 6

outer_function()
print("Global:", x)  # Output: Global: 10

def greet(message):
    def prefix():
        return "Hello, "
    return prefix() + message

print(greet("World"))  # Output: Hello, World


# Built-In Functions:
# Python provides built-in functions like len, sum, min, max, etc.

# Example:

numbers = [1, 2, 3, 4, 5]
print(len(numbers))  # Output: 5
print(sum(numbers))  # Output: 15

# Argument Passing:
# Positional Arguments
# Keyword Arguments
# Default Arguments


def greet(name, message="Hello"):
    print(f"{message}, {name}!")

greet("saad")  # Output: Hello, saad!
greet("Bob", "Hi")  # Output: Hi, Bob!


# Lambda Functions (Anonymous Functions):
# Short, inline functions.

square = lambda x: x**2
print(square(5))  # Output: 25

add = lambda x, y: x + y
print(add(3, 7))  # Output: 10


# --------------------------------

# 3.2 Decorators and Generators
# Decorators:
# A decorator modifies the behavior of a function or method.

def decorator(func):
    def wrapper():
        print("Before the function call")
        func()
        print("After the function call")
    return wrapper

@decorator
def say_hello():
    print("Hello!")

say_hello()
# Output:
# Before the function call
# Hello!
# After the function call


# Generators:
# Generators allow lazy evaluation, yielding items one at a time.

def my_generator():
    for i in range(3):
        yield i

gen = my_generator()
print(next(gen))  # Output: 0
print(next(gen))  # Output: 1
print(next(gen))  # Output: 2


# -------------------------------

# 3.3 Module Basics
# ❖ A MODULE is a file containing other Python constructs like class, functions,variables,statements which together
# perform some specific task(s)
# ❖ Each module needs to have some name and the file should be stored with .py extension.
# ❖ A module acts as a CODE LIBRARY.
# ❖ There are over 200 Standard Library Modules in Python
# ❖ We can create our own USER DEFINED modules and use those in other Python programs to achieve that
# functionality.
# ❖ Having modules means separating a bigger, lengthy code into manageable files each containing some independent
# part of that code.
# ❖ Modules promote modularization of code, code reuse, code maintainability and better organisation.


# Using Built-in Modules:
# Examples with math, random, and datetime:

import math
print(math.sqrt(16))  # Output: 4.0

import random
print(random.randint(1, 10))  # Random number between 1 and 10

import datetime
print(datetime.datetime.now())  # Current date and time

# Map, Filter, Reduce:

numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x**2, numbers))
print(squared)  # Output: [1, 4, 9, 16]


even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4]


from functools import reduce
product = reduce(lambda x, y: x * y, numbers)
print(product)  # Output: 24


# Packages

# ❖ One can think of a folder while thinking of the concept of a PACKAGE. Like a folder, a package is way we can pack
# modules and other components into one wrapper.
# ❖ They boost code reuse and maintainability.
# ❖ A package is a namespace where that package’s modules are bound together by the package name, by which they
# may be referenced in other files.
# ❖ Every package is a module — but not every module is a package.
# ❖ A package folder usually contains one file named __init__.py that tells Python that the given folder/namespace is a
# package. The init file may be empty, or it may contain code to be executed upon package initialization.
# ❖ Python comes with a big collection of pre-installed packages known as the Python Standard Library

# Import Basics:
# Use import to access modules and packages.

import math
print(math.pi)  # Output: 3.141592653589793


# User-Defined Modules:
# Create a module named mymodule.py:

# mymodule.py
def greet(name):
    print(f"Hello, {name}!")

# Use it in another file:
    
# import mymodule
# mymodule.greet("saad")  # Output: Hello, saad!


# ---------------------------

# Asyncio and FastAPI Introduction

# Asyncio: For asynchronous programming.
# for asyncronous programming 

import asyncio

async def say_hello():
    print("Hello, World!")
    await asyncio.sleep(1)
    print("Hello again!")

asyncio.run(say_hello())

# Hello, World!
# <1-second pause>
# Hello again!



# FastAPI: A modern web framework for building APIs.

# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/")
# def read_root():
#     return {"message": "Welcome to FastAPI"}
