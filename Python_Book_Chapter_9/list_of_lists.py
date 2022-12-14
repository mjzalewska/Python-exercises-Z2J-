"""
Challenge 9.4
"""

import statistics

universities = [
['California Institute of Technology', 2175, 37704],
['Harvard', 19627, 39849],
['Massachusetts Institute of Technology', 10566, 40732],
['Princeton', 7802, 37000],
['Rice', 5879, 35551],
['Stanford', 19535, 40569],
['Yale', 11701, 40500]
]


def enrollment_stats(uni_list):
    student_enrollment = [uni[1] for uni in uni_list]
    tuition_fees = [uni[2] for uni in uni_list]

    return student_enrollment, tuition_fees


def calculate_mean(num_list):
    return sum(num_list)/len(num_list)


def calculate_median(num_list):
    return statistics.median(num_list)


def print_stats(stats):
    students, fees = stats
    print(f"Total students: {sum(students):,.0f}")
    print(f"Total tuition: $ {sum(fees):,.0f}\n")
    print(f"Student mean: {calculate_mean(students):,.2f}")
    print(f"Student median: {calculate_median(students):,.0f}\n")
    print(f"Tuition mean: $ {calculate_mean(fees):,.2f}")
    print(f"Tuition median: $ {calculate_median(fees):,.2f}\n")


print_stats(enrollment_stats(universities))
