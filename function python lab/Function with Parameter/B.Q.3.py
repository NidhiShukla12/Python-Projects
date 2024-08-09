

# How can you use parameters to make a function more flexible or reusable?


# Parameters are a fundamental feature of functions that significantly enhance their flexibility and reusability. Here’s how you can leverage parameters to achieve these goals:

# 1. Generalization
# Parameters allow you to write functions that can handle a variety of inputs rather than hardcoding values. This makes your functions more versatile.


def add(x, y):
    return x + y

print(add(2, 3))  # Outputs: 5
print(add(10, 20))  # Outputs: 30

# 2. Default Values
# Parameters can have default values, allowing functions to be called with fewer arguments than defined. This can simplify function calls and make functions more adaptable.

def greet(name="Guest"):
    return f"Hello, {name}!"

print(greet())        # Outputs: Hello, Guest!
print(greet("Alice")) # Outputs: Hello, Alice!

# 3. Keyword Arguments
# Some languages support passing arguments by name (keyword arguments), which improves readability and allows arguments to be specified in any order.

def describe_person(name, age, city):
    return f"{name} is {age} years old and lives in {city}."

print(describe_person(name="Alice", city="New York", age=30))

# 4. Variable-Length Arguments
# Functions can be designed to accept a variable number of arguments, allowing them to handle a flexible number of inputs.

def concatenate(*args):
    return " ".join(args)

print(concatenate("Hello", "world", "from", "Python"))  # Outputs: Hello world from Python