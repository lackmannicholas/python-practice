import numpy as np

array = np.array([1,2,3,4,5])

print(array)

array = np.array([[1,2],[1,2]])
print(array.shape)

# 2x2 array from 0-1
print(np.random.rand(2,2))

# fill 3x4 array with the number 7
print(np.full((3,4), 8))

array = np.array([140, 174, 166, 192])

print(array / 2.2)

# full array populated with 1's
array = np.ones((3,4))
print(array)

# changing the dimensions of the array
print(array.reshape(2,6))

print(array.flatten())


array = np.array([[3,12,11],[45,22,11],[56,15,22]])
# represent all matching conditions
print(array < 20)

# get values that matach a condition
print(array[array < 20])

# horizontally stacking two arrays
# must have same number of dimensions!
first = np.full((2, 12), 2)
print(first)
second = np.full((2, 7), 2)
print(second)
print(np.hstack((first, second)))

# stacking vertically
first = np.full((3,3), 1)
print(first)
second = np.full((3,3), 2)
print(second)
print(np.vstack((first, second)))

array = np.arange(1, 11)
print(array)

# split array in 2 horizontally
print(np.hsplit(array, 2))

# this allows for "unpacking"
first, second = np.hsplit(array, 2)
print(first)
print(second)