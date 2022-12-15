"""
Challenge 8.8
Write a simulation that runs ten thousand trials of the experiment and prints the
average number of flips per trial needed for the sequence to contain both heads and tails
"""

import random


# def simulate(num_of_flips):
#
#     flips = 0
#     results = []
#
#     while flips < num_of_flips:
#         results.append(random.choice(['heads', 'tails']))
#         flips += 1
#
#     count = 1
#     for i in range(len(results)):
#         if results[i] == results[i + 1]:
#             count += 1
#         else:
#             break

# 1. rzucam aż wypadnie przeciwna strona i liczę rzuty
# 2. robię to x razy

def simulate(num_of_flips):

    flips = 0
    results = []

    while flips < num_of_flips:
        results.append(random.choice(['heads', 'tails']))
        flips += 1

    count = 1
    for i in range(len(results)):
        if results[i] == results[i + 1]:
            count += 1
        else:
            break






















