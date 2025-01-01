## Pandas Plot ----
#1) hist() - df.hist(column = ['columns Name'], bins = Bin Number)
#2) scatter() - df.plot.scatter(x='column name', y='column name')
#3) boxplot() - df.boxplot(column = ['columnName1', 'columnName2'])



## Numpy -------
#1) arr.ndim  = Number of Dimensions
#In Python we have lists that serve the purpose of arrays, but they are slow to process.
#NumPy aims to provide an array object that is up to 50x faster than traditional Python lists
import numpy as np
l = [3,4,5,6,6]
a = np.array(l)
# print(a)
# print(type(a))
# print(a[2])
# print(l)
# print(type(l))

# 2D Array -----------------------------------------
D2a = np.array([[2,3,4], [4,5,6]])
print(D2a[1,2])