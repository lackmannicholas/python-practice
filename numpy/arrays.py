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

array = np.ones((3,4))
print(array)

print(array.reshape(2,6))

print(array.flatten())