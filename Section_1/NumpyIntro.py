Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import numpy
>>> 
>>> import numpy as np
>>> arr = np.array([2,4,7,9,1,4,5,6,7,8])
>>> type(arr)
<class 'numpy.ndarray'>
>>> arr.shape
(10,)
>>> x = 10
>>> type(x)
<class 'int'>
>>> x = 10,
>>> type(x)
<class 'tuple'>
>>> arr = np.array([2,4,7,9,1,4,5,6,7,8,'Hi','Hello'])
>>> arr
array(['2', '4', '7', '9', '1', '4', '5', '6', '7', '8', 'Hi', 'Hello'],
      dtype='<U11')
>>> arr = np.array([2,4,7,9,1,4,5,6,7,8,12.5])
>>> arr
array([  2. ,   4. ,   7. ,   9. ,   1. ,   4. ,   5. ,   6. ,   7. ,
         8. ,  12.5])
>>> arr = np.array([2,4,7,9,1,4,5,6,7,8])
>>> list_1 = [['Ram',25,'HCL'],['Shyam',28,'Wipro'],['Mohan',24,'TCS']]
>>> list_1
[['Ram', 25, 'HCL'], ['Shyam', 28, 'Wipro'], ['Mohan', 24, 'TCS']]
>>> arr_1 = np.array([['Ram',25,'HCL'],['Shyam',28,'Wipro'],['Mohan',24,'TCS']])
>>> arr_1
array([['Ram', '25', 'HCL'],
       ['Shyam', '28', 'Wipro'],
       ['Mohan', '24', 'TCS']],
      dtype='<U5')
>>> arr_1.shape
(3, 3)
>>> arr_1[2][2]
'TCS'
>>> np.rank(arr_1)

Warning (from warnings module):
  File "__main__", line 1
VisibleDeprecationWarning: `rank` is deprecated; use the `ndim` attribute or function instead. To find the rank of a matrix see `numpy.linalg.matrix_rank`.
2
>>> np.ndim(arr_1)
2
>>> arr_1
array([['Ram', '25', 'HCL'],
       ['Shyam', '28', 'Wipro'],
       ['Mohan', '24', 'TCS']],
      dtype='<U5')
>>> arr_1.transpose()
array([['Ram', 'Shyam', 'Mohan'],
       ['25', '28', '24'],
       ['HCL', 'Wipro', 'TCS']],
      dtype='<U5')
>>> arr_2 = np.arange(5)
>>> arr_2
array([0, 1, 2, 3, 4])
>>> arr_2 = np.arange(5,10)
>>> arr_2
array([5, 6, 7, 8, 9])
>>> arr_2 = np.arange(5,51,5)
>>> arr_2
array([ 5, 10, 15, 20, 25, 30, 35, 40, 45, 50])
>>> import random
>>> random.randint(0,100)
37
>>> np.random.randint(1,50)
34
>>> arr_3 = np.random.randint(1,50,10)
>>> arr_3
array([ 2, 48, 46, 28, 13, 18, 49, 26,  3, 22])
>>> x = np.random.randint(1,50,10)
>>> y = np.arange(1,11)
>>> x
array([35,  2, 17, 16, 33, 12, 12,  9, 47, 16])
>>> y
array([ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10])
>>> x = np.arange(1,11)
>>> y = np.random.randint(1,50,10)
>>> x = np.random.randint(1,50,10)
>>> y = np.arange(1,11)
>>> x
array([47, 44, 32, 18, 30, 21, 31, 21, 30, 42])
>>> y
array([ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10])
>>> x,y = y,x
>>> x
array([ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10])
>>> y
array([47, 44, 32, 18, 30, 21, 31, 21, 30, 42])
>>> import matplotlib.pyplot as plt
>>> plt.plot(x,y)
[<matplotlib.lines.Line2D object at 0x0000022234D8BCF8>]
>>> plt.show()
>>> x = np.arange(1,1000)
>>> y = np.random.randint(1,50000,1000)
>>> len(x)
999
>>> len(y)
1000
>>> x = np.arange(1,1001)
>>> len(x)
1000
>>> plt.plot(x,y)
[<matplotlib.lines.Line2D object at 0x000002223527EB70>]
>>> plt.show()
>>> 
