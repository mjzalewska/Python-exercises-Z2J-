"""
Challenge 8.9
Suppose two candidates, Candidate A and Candidate B, are running for mayor in a city with three voting regions.
The most recent polls show that Candidate A has the following chances of winning in each region:
Region 1: 87% chance of winning
Region 2: 65% chance of winning
Region 3: 17% chance of winning
Write a program that simulates the election then thousand times and prints the % of times in which Candidate A wins.
Assume that a candidate wins the election if they win in at least two of the three regions.
"""

import random


victory_prob = [.87, .65, .17]


def election_win(a_probabilities):

    win = 0
    loss = 0

    for prob in a_probabilities:
        if random.random() < prob:
            win += 1
    else:
        loss += 1

    if win >= 2:
        return 'A'
    else:
        return 'B'


def simulate_election(trials, probability_matrix):
    trial = 0
    a_wins = 0
    b_wins = 0

    while trial < trials:
        if election_win(probability_matrix) == 'A':
            a_wins += 1
        else:
            b_wins += 1
        trial += 1

    a_wins_percentage = a_wins / trials * 100
    b_wins_percentage = b_wins / trials * 100
    print(f"The probability Candidate A wins when the simulation is run {trials} times is {a_wins_percentage:.2f} %")
    print(f"The probability Candidate B wins when the simulation is run {trials} times is {b_wins_percentage:.2f} %")
    return a_wins_percentage, b_wins_percentage


simulate_election(10000, victory_prob)
