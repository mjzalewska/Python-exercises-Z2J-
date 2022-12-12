"""
Challenge 5.3
Write a program that receives two numbers from the user and displays the first number
raised to the power of the second number.
"""

base = input("Enter a base: ")
exponent = input("Enter an exponent: ")

result = float(base) ** float(exponent)
print(f"{base} to the power of {exponent} is {round(result, 2)}")