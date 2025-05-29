import numpy as np 
print(np.__version__)

array_2d= np.array([[1,2,3,4,5],
          [6,7,8,9,10]])

print(array_2d)

element = array_2d[0,3]
print(element)

dimesions = array_2d.ndim
print(dimesions)

size = array_2d.size
print(size)

total_sum = np.sum(array_2d)
print(total_sum)

total_col = np.sum(array_2d, axis=0)
print(total_col)

total_row = np.sum(array_2d, axis=1)
print(total_row)