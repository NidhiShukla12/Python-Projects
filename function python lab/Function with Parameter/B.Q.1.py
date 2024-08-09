

# Q.1 How do you define a function that takes parameters?

# Defining a function that takes parameters involves specifying the parameters in the function's definition. Parameters are placeholders for the values that will be passed to the function when it is called. They allow the function to operate on different inputs each time it is invoked.

# Defining a Function with Parameters:

def greet(name):
    return f"Hello, {name}!"

# Calling the Function with an Argument:

message = greet("Alice")
print(message)  # Outputs: Hello, Alice!