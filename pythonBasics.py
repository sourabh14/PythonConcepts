# Introduction to Python

# 1. Variables and Data Types
print("1. Variables and Data Types")
name = "Alice"         # string
age = 25               # integer
height = 5.7           # float
is_student = True      # boolean

print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Is a student:", is_student)
print()

# 2. Basic Operations
print("2. Basic Operations")
x = 10
y = 3
print("x + y =", x + y)
print("x - y =", x - y)
print("x * y =", x * y)
print("x / y =", x / y)
print("x // y =", x // y)   # floor division
print("x % y =", x % y)     # modulus
print("x ** y =", x ** y)   # exponent
print()

# 3. Conditional Statements
print("3. Conditional Statements")
if age >= 18:
    print(f"{name} is an adult.")   # formatted output
else:
    print(f"{name} is not an adult.")
print()

# 4. Loops
print("4. Loops")
print("For Loop:")
for i in range(5):  # Loop from 0 to 4
    print("i =", i)

print("While Loop:")
count = 0
while count < 3:
    print("count =", count)
    count += 1
print()

# 5. Functions
print("5. Functions")

def greet(person_name):
    print(f"Hello, {person_name}!")

greet(name)

def add(a, b):
    return a + b

result = add(10, 5)
print("10 + 5 =", result)
print()

# 6. Lists and List Operations
print("6. Lists and List Operations")
fruits = ["apple", "banana", "cherry"]
print("Fruits:", fruits)

# Adding an item
fruits.append("orange")
print("After adding 'orange':", fruits)

# Removing an item
fruits.remove("banana")
print("After removing 'banana':", fruits)

# Looping through a list
print("Fruits in the list:")
for fruit in fruits:
    print(fruit)

# List comprehension
squared_numbers = [x**2 for x in range(5)]
print("Squared numbers:", squared_numbers)
print()

# 7. Tuples and Sequences
print("7. Tuples and Sequences")
# Tuples are used to store multiple items in a single variable.
# Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary
# Tuples are immutable sequences
# Tuples use less memory and are faster to access than to lists.
# If you have data that shouldn’t change, you should choose tuple data type over lists. Typically used for fixed collections of items, such as coordinates, database records
colors = ("red", "green", "blue")  # Tuple
print("Colors tuple:", colors)
print("First color:", colors[0])

# Tuple unpacking
r, g, b = colors
print("Unpacked colors:", r, g, b)

# List of tuples
points = [(1, 2), (3, 4), (5, 6)]
for x, y in points:
    print(f"Point: x={x}, y={y}")
print()

# 8. Dictionaries
print("8. Dictionaries")
person = {
    "name": "Alice",
    "age": 25,
    "is_student": True
}
print("Person Dictionary:", person)
print("Name:", person["name"])
print("Age:", person["age"])
print("Is a student:", person["is_student"])
print()

# 9. Exception Handling
print("9. Exception Handling")

try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
else:
    print("Division result:", result)
finally:
    print("End of exception handling block.")
print()

# 10. Classes
print("10. Classes")

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# Creating an instance of the Person class
person1 = Person("Alice", 25)
person1.greet()

# Inheritance example
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def display_student_info(self):
        print(f"Student ID: {self.student_id}")

# Creating an instance of the Student class
student1 = Student("Bob", 20, "S12345")
student1.greet()
student1.display_student_info()
print()

# 11. Summary
print("That's a quick introduction to Python, covering some fundamental concepts!")
