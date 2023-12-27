### NUMPY ###
import numpy as np
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print(matrix)
# [[1 2 3]
#  [4 5 6]
#  [7 8 9]]

# accessing matrix elements:
# matrix[0][1] #2
# matrix[0, 1]

# np arrays can only hold objects of the SAME TYPE
# np performs automatic data type converson (when two types of data are added to the matrix - np will convert it to one,
# e.g. string + num will result to all data being coverted to string)

## ARRAY OPERATIONS (performed element-wise)
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
B = A * 2
# print(B)
# [[ 2  4  6]
#  [ 8 10 12]
#  [14 16 18]]

C = B - A
# print(C_prime)

E = np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
D = E @ E
# print(E)
# print(D)
# [[3 3 3]
#  [3 3 3]
#  [3 3 3]]

## BASIC OPERATIONS

# # axis length
# print(A.shape)
#
# # matrix diagonal
# print(A.diagonal())
#
# # flattening
# print(A.flatten())
#
# # transpose
# print(A.transpose())
#
# # min value
# print(A.min())
#
# # max value
# print(A.max())
#
# # mean value
# print(A.mean())
#
# # sum of all entries
# print(A.sum())

## STACKING

G = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
H = np.array([[10, 11, 12], [13, 14, 15], [16, 17, 18]])

# vertically
# print(np.vstack([G, H]))
# # [[ 1  2  3]
# #  [ 4  5  6]
# #  [ 7  8  9]
# #  [10 11 12]
# #  [13 14 15]
# #  [16 17 18]]

# horizontally
# print(np.hstack([G, H]))
# # [[ 1  2  3 10 11 12]
# #  [ 4  5  6 13 14 15]
# #  [ 7  8  9 16 17 18]]

## RESHAPE
# print(A.reshape(9, 1))
# .reshape() returns a new array

## ARANGE
K = np.arange(1,10)
print(K)

matrix_K = K.reshape(3, 3)
# print(matrix_K)

L = np.arange(1, 17).reshape(4, 2, 2)
# print(L)
# # [[[ 1  2]
# #   [ 3  4]]
# #
# #  [[ 5  6]
# #   [ 7  8]]
# #
# #  [[ 9 10]
# #   [11 12]]
# #
# #  [[13 14]
# #   [15 16]]]

## REVIEW EXERCISES

"""(1) Use np.arange() and np.reshape() to create a 3 x 2 NumPy array named A
that includes the numbers 3 through 11"""
A = np.arange(3, 12).reshape(3, 3)
# print(A)

"""(2) Display the minimum, maximum, and mean of all entries in A"""
# print(A.min())
# print(A.max())
# print(A.mean())

"""(3) Square every entry in A using the ** operator 
and save the results in an array named B"""
B = A ** 2
# print(B)

"""(4) Use np.vstack() to stack A on top of B, 
then save the results to an array named C_prime"""
C_prime = np.vstack([A, B])
print(C_prime)

