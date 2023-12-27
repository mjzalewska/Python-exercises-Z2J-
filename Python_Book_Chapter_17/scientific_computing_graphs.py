import csv

from matplotlib import pyplot as plt
import numpy as np
from numpy import random

# plt.plot([1, 2, 3, 4, 5])
# list represents the y-values, list element indices are used as x-values
# if two arguments (lists) are passed to plt.plot - the first one represents x values,
# and the second one - y values.
# plt.show()

xs = [1, 2, 3, 4, 5]
ys = [2, 4, 6, 8, 10]
# plt.plot(xs, ys)
# plt.show()

new_xs = [1, 2, 3, 4, 5]
new_ys = [3, -1, 4, 0, 6]
# plt.plot(new_xs, new_ys)
# plt.show()

# plt.plot([2, 4, 6, 8, 10], "g-o")
# plt.show()

## USING NUMPY FOR STORING/ GENERATING PLOT DATA
# data_points = np.arange(1, 6)
# plt.plot(data_points, "y-^")
# plt.show()

# plot the columns
# data = np.arange(1, 21).reshape(5, 4)
# print(data)
# # [[ 1  2  3  4]
# #  [ 5  6  7  8]
# #  [ 9 10 11 12]
# #  [13 14 15 16]
# #  [17 18 19 20]]
# plt.plot(data.transpose())
# plt.show()
# plot the rows
# plt.plot(data)
# plt.show()

## FORMATTING PLOTS ##

days = np.arange(0, 21)
other_site, real_python = days, days ** 2
plt.plot(days, other_site, "r-o")
plt.plot(days, real_python, "b-^")
plt.xticks([0, 5, 10, 15, 20])  # adjust the x-axis
plt.xlabel("Days of reading")
plt.ylabel("Amount of Python learnt")
plt.title("Python learnt reding Real Python vs other site")
plt.legend(["Other site", "Real Python"])
plt.show()

## BARCHARTS

centers = np.arange(1, 6)
tops = np.arange(2, 11, 2)

# plt.bar(centers, tops) # the first argument can be a list of nums or a list of strings
# representing categories of data
# plt.show()

fruits = {
    "apples": 10,
    "oranges": 16,
    "bananas": 9,
    "pears": 4
}
# plt.bar(fruits.keys(), fruits.values())
# plt.show()

## HISTOGRAMS

# plt.hist(value_list, no_of_bins)
plt.hist(random.randn(10000), 20)

# saving the graph to the current working directory
# to save elsewhere - provide absolute path
# ALWAYS save the graph before calling plt.show()
plt.savefig("fig_1.png")

# plt.show()

## REVIEW EXERCISES

""" Do pirates cause global warming? Write a program that visually examines this
relationship by reading the pirates.csv file and graphing the number of pirates 
along the x-axis and the temperature along the y-axis. Add a title and label the 
graph's axes, then save the resulting graph as a PNG image file"""

with open("C:\\Users\\mjarz\\Downloads\\pirates.csv", "r") as file:
    data = list(csv.reader(file))
    years = [int(item[0]) for item in data[1:]]
    temperature = [float(item[1]) for item in data[1:]]
    pirates = [int(item[2]) for item in data[1:]]


plt.plot(pirates, temperature, "r-o")
plt.title("Number of pirates vs global temperatures")
plt.xlabel("Total pirates")
plt.ylabel("Average global temperature")
plt.axis([-300, 48000, 14, 16]) #(xmin, xmax, ymin, ymax)

# annotate the plotted points with years
for i in range(0, len(years)):
    plt.annotate(str(years[i]), xy=(pirates[i], temperature[i]))

plt.savefig("fig_2.png")
plt.show()
