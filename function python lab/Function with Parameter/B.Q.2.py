
# What are the rules for passing arguments to a function?


# When passing arguments to a function, there are several rules and best practices to keep in mind. These can vary slightly depending on the programming language, but many principles are consistent across languages:

def example(a, b, c=3):
    print(a, b, c)

example(1, 2)          # Outputs: 1 2 3 (uses default value for c)
example(1, 2, 4)       # Outputs: 1 2 4
example(a=1, b=2)      # Outputs: 1 2 3 (uses default value for c)