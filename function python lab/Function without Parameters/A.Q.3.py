
# Q.3 Can a function without parameters return a value? If so, how?


# Yes, a function without parameters can indeed return a value. The key is that the function can still perform computations or retrieve data internally, and then return a result. The absence of parameters simply means that the function does not take any inputs when it is called.

# Defining a Function:

def get_greeting():
    return "Hello, world!"


# Calling the Function and Using the Return Value:

greeting = get_greeting()
print(greeting)  # Outputs: Hello, world!