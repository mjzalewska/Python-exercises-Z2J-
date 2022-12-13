"""
Challenge 6.3
Write a program called temperature.py that defines two functions:

1. convert_cel_to_far(), which takes one float parameter representing degrees Celsius and returns a float representing
the same temperature in degrees Fahrenheit using the following formula:
F = C * 9/5 + 32
2. convert_far_to_cel(), which takes one float parameter representing degrees Fahrenheit and returns a float
representing the same temperature in degrees Celsius using the following formula:
C = (F - 32) * 5/9
"""


def get_input():
    print("Please provide the temperature you would like to convert: ")
    while True:
        user_input = input()
        if not user_input.isdigit():
            print("This is not a valid input. Please provide temperature (numeric value): ")
        else:
            return float(user_input)


def convert_cel_to_far(c_temp):
    cel_to_far = c_temp * 9 / 5 + 32
    print(f"You have entered: {c_temp} Celsius")
    print(f"The Fahrenheit equivalent is: {cel_to_far}")
    return cel_to_far


def convert_far_to_cel(f_temp):
    far_to_cel = (f_temp - 32) * 5 / 9
    print(f"You have entered: {f_temp} Fahrenheit")
    print(f"The Celsius equivalent is: {far_to_cel}")
    return round(far_to_cel,2)

# convert_cel_to_far(get_input())
# convert_far_to_cel(get_input())