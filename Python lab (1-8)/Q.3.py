
# Q.3 Write a program for Bitwise operators.

# A bitwise operator is a symbol used in programming languages to perform operations on binary numbers (numbers represented in base 2) at the bit level. These operators work directly on the individual bits of a number, allowing for manipulation of the binary representation of a value

# Bitwise And: a & b
# Bitwise Or: a | b
# Bitwise Xor: a ^ b
# Bitwise Not: ~a
# Left Shift: a << b
# Right Shift: a >> b

# Bitwise And: a & b

a = 60  # Binary: 0011 1100
b = 13  # Binary: 0000 1101
result = a & b  # Binary: 0000 1100
print(result)  # Output: 12

# Bitwise Or: a | b

a = 60  # Binary: 0011 1100
b = 13  # Binary: 0000 1101
result = a | b  # Binary: 0011 1101
print(result)  # Output: 61

# Bitwise Xor: a ^ b

a = 60  # Binary: 0011 1100
b = 13  # Binary: 0000 1101
result = a ^ b  # Binary: 0011 0001
print(result)  # Output: 49

# Bitwise Not: ~a

a = 60  # Binary: 0011 1100
result = ~a  # Binary: 1100 0011 (inverted bits)
print(result)  # Output: -61

# Left Shift: a << b

a = 60  # Binary: 0011 1100
shift = 2
result = a << shift  # Binary: 1111 0000
print(result)  # Output: 240

# Right Shift: a >> b

a = 60  # Binary: 0011 1100
shift = 2
result = a >> shift  # Binary: 0000 1111
print(result)  # Output: 15
