# chapter 1

# data types : 

# int, float

# list, tuple

# str

# dict

# set

# bool

# -----------------------
# Operators in Python
# Arithmetic Operators: +, -, *, /, %, //, **
# Comparison Operators: ==, !=, <, >, <=, >=
# Logical Operators: and, or, not
# Bitwise Operators: &, |, ^, ~, <<, >>
# Assignment Operators: =, +=, -=, etc.
# Membership Operators: in, not in

# Arithmetic and Logical Example
a = 10
b = 20
print(a + b)        # 30
print(a > 5 and b < 25)  # True


# Numbers
num = 10.5
print(type(num))  # <class 'float'>

# Strings
s = "Hello, Python!"
print(s.upper())  # HELLO, PYTHON!

# Lists
lst = [1, 2, 3]
lst.append(4)
print(lst)  # [1, 2, 3, 4]

# Dictionaries
d = {"name": "saad", "age": 22}
print(d["name"])  # saad

# Tuples
t = (1, 2, 3)
print(t[1])  # 2

# Printing the range directly
print(range(5))  # Output: range(0, 5)

# Converting range to a list to see the numbers
print(list(range(5)))  # Output: [0, 1, 2, 3, 4]

# Specifying a start and stop
print(list(range(2, 6)))  # Output: [2, 3, 4, 5]

# Specifying a step
print(list(range(1, 10, 2)))  # Output: [1, 3, 5, 7, 9]

# Key Points:
# 1  range(stop): Generates numbers from 0 to stop-1.
# 2 range(start, stop): Starts from start and goes up to stop-1.
# 3 range(start, stop, step): Adds a step to control the increment.
# You need to convert the range object to a list (or loop through it) to see its elements.

# -------------------------

# 1.3 Python Blocks and Program Flow Control
# Python Blocks:
# Blocks are indented sections of code.

# Conditional Blocks:
# Use if, else, and elif to branch logic.
# Loops:
# For Loop: Iterates over a sequence.
# While Loop: Runs while a condition is true.
# Special Keywords:
# pass: Do nothing.
# break: Exit the loop.
# continue: Skip the rest of the code in the current iteration.
# else: Executes if the loop ends normally.

# Conditional Blocks
x = 10
if x > 5:
    print("Greater than 5")
elif x == 5:
    print("Equals 5")
else:
    print("Less than 5")

# # Loops
for i in range(3):
    if i == 1:
        continue  # Skip 1
    print(i)  # Prints 0, 2
else:
    print("Loop finished")

# ------------------------

# 1.4 File Operations
# Reading Functions:
# read(): Reads the entire file.
# readline(): Reads a single line.
# readlines(): Reads all lines into a list.
# Writing Functions:
# write(): Writes a string to a file.
# writelines(): Writes a list of strings.
# Manipulating File Pointer:
# seek(offset): Moves the pointer to a specific location in the file.

# # Writing to a file
with open("example.txt", "w") as f:
    f.write("Hello, File!\n")
    f.writelines(["Line 1\n", "Line 2\n"])

# Reading from a file
with open("example.txt", "r") as f:
    print(f.read())           # Reads entire content
    f.seek(0)                 # Move pointer to start
    print(f.readline())       # Reads one line
    print(f.readlines())      # Reads all lines as list

