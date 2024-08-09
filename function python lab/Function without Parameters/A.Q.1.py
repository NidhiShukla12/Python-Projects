

# Q.2 What is a function without parameters, and when might you use one?


# A function without parameters is a function that doesn't take any input values when it's called. Instead of accepting arguments, it operates using values that are either hardcoded within the function or that it derives from other internal state or global variables.

def greet():
    print("Hello, world!")

# When you call greet(), it will always print "Hello, world!"

def initialize_app():
    print("Application initialized!")

initialize_app()

# Status checked or initialized

def print_status():
    print("System is operational.")

print_status()

 # Utility functions

def print_welcome_message():
    print("Welcome to our service!")

print_welcome_message()

#Event Handlers

def on_click():
    print("Button clicked!")

on_click()

# Time-based Functions

def perform_backup():
    print("Backup performed!")

perform_backup()