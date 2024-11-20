# chapter 2


# Class: A blueprint for creating objects (data structures). It defines properties (attributes) and behaviors (methods).

# Object: An instance of a class.

class Person:   # class keyword used 
    # Constructor to initialize attributes
    def __init__(self, name, age):
        self.name = name  # Instance variable
        self.age = age

    # Method
    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# Creating an object (instance of the class)
person1 = Person("saad", 22)

# Accessing class members (attributes and methods)
print(person1.name)  # Output: saad
print(person1.age)   # Output: 22
person1.greet()      # Output: Hello, my name is saad and I am 22 years old.


# ----------------------------

# 2.2 Setter and Getter Methods
# Setter: Updates the value of an attribute.
# Getter: Retrieves the value of an attribute.

class Person:
    def __init__(self, name, age):
        self.__name = name  # Private variable
        self.__age = age

    # Getter for name
    def get_name(self):
        return self.__name

    # Setter for name
    def set_name(self, name):
        self.__name = name

    # Getter for age
    def get_age(self):
        return self.__age

    # Setter for age
    def set_age(self, age):
        if age > 0:  # Validation
            self.__age = age
        else:
            print("Age must be positive!")

# Example usage
p = Person("saad", 22)
print(p.get_name())  # Output: saad
p.set_name("Bob")
print(p.get_name())  # Output: Bob
p.set_age(-5)        # Output: Age must be positive!
p.set_age(30)
print(p.get_age())   # Output: 30



# -----------------------------

# 2.3 Constructor and Destructor
# Constructor: A method automatically called when an object is created. In Python, this is the __init__ method.
# Destructor: A method called when an object is deleted. In Python, this is the __del__ method.
# Example:

class Person:
    def __init__(self, name):
        self.name = name
        print(f"{self.name} is created!")

    def __del__(self):
        print(f"{self.name} is deleted!")

# Example usage
p1 = Person("saad")  # Output: saad is created!
del p1                # Output: saad is deleted!



# ------------------------------

# 2.4 Inheritance, Superclass, and Operator Overloading
# Inheritance: A class (child) can inherit attributes and methods from another class (parent).
# Superclass: The parent class in inheritance.
# Operator Overloading: Redefining how operators work for objects.

# Parent class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")

# Child class inheriting from Animal
class Dog(Animal):
    def speak(self):
        print(f"{self.name} barks!")

# Example usage
a = Animal("Generic Animal")
a.speak()  # Output: Generic Animal makes a sound.

d = Dog("Rex")
d.speak()  # Output: Rex barks!

# Operator overloading
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"Point({self.x}, {self.y})"

p1 = Point(1, 2)
p2 = Point(3, 4)
print(p1 + p2)  # Output: Point(4, 6)


# ------------------------------

# 2.5 Static and Class Methods
# Static Method: A method that doesn’t depend on the instance or class; it’s like a regular function within a class.
# Class Method: A method that works with the class itself instead of instances.

class MyClass:
    count = 0  # Class variable

    def __init__(self):
        MyClass.count += 1

    @staticmethod
    def greet():
        print("Hello! This is a static method.")

    @classmethod
    def get_count(cls):
        return f"Total instances created: {cls.count}"

# Example usage
# without creating a obj we can just create a object 
MyClass.greet()  # Output: Hello! This is a static method.
obj1 = MyClass()
obj2 = MyClass()
print(MyClass.get_count())  # Output: Total instances created: 2


# -----------------------------
# 2.6 Delegation and Container
# Delegation: Forwarding functionality from one object to another.
# Container: An object that holds and manages other objects.

# Example of Delegation:
# delegation means dividing the load  and creating results with others 

# example when we have to do similar operations in 2 different class then we can just make a oject of 1st class in the 2nd class and the operation can be solved here 

# 2nd class is container and 1st is contained 

class Engine:
    def start(self):
        print("Engine started.")

class Car:
    def __init__(self):
        self.engine = Engine()  # Delegation

    def start(self):
        print("Car is starting...")
        self.engine.start()

# Example usage
c = Car()
c.start()
# Output:
# Car is starting...
# Engine started.

# Example of Container:

class Bag:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def show_items(self):
        print("Bag contains:", self.items)

# Example usage
bag = Bag()
bag.add_item("Book")
bag.add_item("Pen")
bag.show_items()  # Output: Bag contains: ['Book', 'Pen']
