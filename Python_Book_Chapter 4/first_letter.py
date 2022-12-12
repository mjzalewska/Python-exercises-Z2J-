"""
Challenge 4.5
Write a program named first_letter.py that prompts the user to for input with the string "Tell me your password: ".
The program should then determine the first letter of the user's input, convert that letter to uppercase, and
display it back.
"""

user_pass = input("Tell me your password: ")
print(user_pass[0].upper())
