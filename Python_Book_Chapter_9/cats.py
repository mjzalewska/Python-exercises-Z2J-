"""
Challenge 9.9

Always start with the cat #1. Each time you stop at a cat,you check if it has a hat on. If not - you put one on,
if it does - you take it off.
Round #1: stop at every cat, placing a hat on each one
Round #2: stop at every second cat (#2, #4, #6, #8, etc.)
Round #3: stop at every third cat (#3, #6, #9, #12, etc.)
Continue the process until you've made 100 rounds around the cats.
On the last round, you stop only at cat #100.

Write a program which outputs which cats have hats at the end.
"""


def divisor(number):
    return [item for item in range(2, number + 1) if number % item == 0]


cats = {num: "" for num in range(1, 101)}

for key in cats.keys():
    if len(divisor(key)) % 2 == 0:
        cats[key] = True
    elif len(divisor(key)) % 2 != 0:
        cats[key] = False

for key, value in cats.items():
    if value:
        print(f"Cat #{key} has a hat")


