"""
Challenge 8.4
Write a program called factors.py that asks the user to input a positive integer and
then prints out the factors of that number.
"""


def get_input():
    print("Please give a positive integer: ")
    while True:
        user_input = input()
        if (float(user_input)).is_integer() and int(user_input) > 0:
            return user_input
        else:
            print("Sorry this is not a valid response. Please provide a POSITIVE integer!")


def get_factors(number):
    factors = [num for num in range(1, int(number)+1) if int(number)%num == 0]
    for factor in factors:
        print(f"{factor} is a factor of {number}")
    return factors


get_factors(get_input())

