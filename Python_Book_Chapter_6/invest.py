"""
Challenge 6.5
Write a program called invest.py that tracks the growing amount of investment over time.
The initial deposit for an investment is called the principal amount. Each year, the amount increases by a fixed
percentage, called the annual rate of return.
For example, a principal amount of $100.00 with an annual rate of return 5% increases the first year by $5.00 for a new
amount of $105.00. The second year, the increase is 5% of $105.00, or $5.25, bringing the total to $110.25.

Write a function called invest with three parameters: the principal amount, the annual rate of return, and the number of
years to calculate.
"""
import math

user_amount = input("Please provide the initial investment amount: ")
user_rate = input("Please provide the annual rate of return as a number: ")
user_years = input("Please provide the time span of the investment (in years): ")


def invest(amount, rate, years):
    counter = 1
    while counter < float(years) + 1:
        inv_return = (1 + float(rate) / 100) ** counter * float(amount)
        print(f"year {counter}: {round(inv_return, 2)}")
        counter += 1


invest(user_amount, user_rate, user_years)
