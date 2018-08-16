import numpy as np


# 1. Let's create a numpy array from a list.
# a. Import the "numpy" library as "np".
# b. Create a list with values 1 to 10 and assign it to the variable "x".
# c. Create an integer array from "x" and assign it to the variable "a1".
# d. Create an array of floats from "x" and assign it to the variable "a2".
# e. Print the data type of each array (use the attribute "dtype").
print("-------- Ejercicio 1 ----------")
x = list(range(1,11))
print(x)

a1 = np.array(x, dtype=int)
print(a1.dtype)

a2 = np.array(x, dtype=float)
print(a2.dtype)

# 2. Let's create arrays in different ways.
# a. Create an array of shape (2, 3, 4) of zeros.
# b. Create an array of shape (2, 3, 4) of ones.
# c. Create an array with values 0 to 999 using the "np.arange" function.
print("-------- Ejercicio 2 ----------")
ZEROS = np.zeros((2,3,4));
print(ZEROS);

ONES = np.ones((2,3,4));
print(ONES);

ARANGE = np.arange(0,1000);
print(ARANGE)


# 3. Let's look at indexing and slicing arrays.
# a. Create an array from the list [2, 3.2, 5.5, -6.4, -2.2, 2.4] and assign it to the
# variable "a".
# b. Do you know what a[1] will equal? Print it to see.
# c. Try printing a[1:4] to see what that equals
# d. Create a 2-D array from the following list and assign it to the variable "a":
# [[2, 3.2, 5.5, -6.4, -2.2, 2.4],
# [1, 22, 4, 0.1, 5.3, -9],
# [3, 1, 2.1, 21, 1.1, -2]]
# e. Can you guess what the following slices are equal to? Print them to check your
# understanding.
# a[:, 3]
# a[1:4, 0:4]
# a[1:, 2]
print("-------- Ejercicio 3 ----------")
a = np.array([2, 3.2, 5.5, -6.4, -2.2, 2.4])
print(a[1])
print(a[1:4])

a = np.array(   [[2, 3.2, 5.5, -6.4, -2.2, 2.4],
                [1, 22, 4, 0.1, 5.3, -9],
                [3, 1, 2.1, 21, 1.1, -2]])

print(a)

print(a[:, 3])
print(a[1:4, 0:4])
print(a[1:, 2])

# 1. Let's interrogate an array to find out its characteristics.
# a. Create a 2-D array of shape (2, 4) containing two lists (range(4), range(10, 14))
# and assign it to the variable "arr".
# b. Print the shape of the array.
# c. Print the size of the array.
# d. Print the maximum and minimum of the array.

print("-------- Ejercicio 4 ----------")

arr = np.array((range(4),range(10,14)))
print(arr)

print(arr.shape)

print(arr.size)

print(np.max(arr))
print(np.min(arr))

# 2. Let's generate new arrays by modifying our array.
# a. Continue to use the array "arr" as defined above.
# b. Print the array re-shaped to (2, 2, 2).
# c. Print the array transposed.
# d. Print the array flattened to a single dimension.
# e. Print the array converted to floats.

print("-------- Ejercicio 5 ----------")

print(np.reshape(arr,(2,2,2)))

print(np.transpose(arr))

print(np.ravel(arr))

print(np.array(arr,dtype=float))





# 1. Let's perform some array calculations.
# a. Create a 2-D array of shape (2, 4) containing two lists (range(4), range(10, 14)) and
# assign it to the variable "a".
# b. Create an array from a list [2, -1, 1, 0] and assign it to the variable "b".
# c. Multiply array "a" by "b" and view the result. Do you understand how NumPy has used its
# broadcasting feature to do the calculation even though the arrays are different shapes?
# d. Multiply array "b" by 100 and assign the result to the variable "b1".
# e. Multiply array "b" by 100.0 and assign the result to the variable "b2".
# f. Print the arrays "b1" and "b2".
# g. Print "b1 == b2". Are they the same?
# h. Why do they display differently? Interrogate the typecode of each array to find out why


print("-------- Ejercicio 6 ----------")

a = np.array((range(4), range(10, 14)))

print(a)

list = list([2, -1, 1, 0] )
b = np.array(list)
print(b)

print(a*b)

b1 = b*100;
print(b1)

b2 = b*100.0
print(b2)

print(b1==b2)

print("Porque b1 es int y b2 es float")


