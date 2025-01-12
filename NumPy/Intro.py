# Numpy is 50X faster than Python List

import numpy as np

'''
we can pass any tuple,list any array like object that converts to a ndarray object
'''
array = np.array((1,2,3,4,5,6,7,8,9))

li = [1,2,3,'a','b','c','d','e','f']
li = np.array(li)
print(li)

print(array)
print(type(array))
print(np.__version__)