"""
Challenge 8.8
Write a simulation that runs ten thousand trials of the experiment and prints the
average number of flips per trial needed for the sequence to contain both heads and tails
"""

import random


def flip_coin():
    if random.choice(['heads', 'tails']) == 'heads':
        return "heads"
    else:
        return "tails"


def simulate(trials):
    flips = 0
    trial = 0

    while trial < trials:
        if flip_coin() == 'heads':
            flips += 1
            while flip_coin() == 'heads':
                flips += 1
            flips += 1

        else:
            flips += 1
            while flip_coin() == 'tails':
                flips += 1
            flips += 1
        trial += 1

    avg_flips = (flips) / trials
    print(f"On average {avg_flips} flips are needed for the sequence to contain both heads and tails if you run "
          f"{trials:,.0f} trials.")
    return avg_flips


simulate(10000)
