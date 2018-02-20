Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import pandas
>>> import pandas as pd
>>> dataset = {'movie_name':[]}
'
>>> 
'
>>> dataset = {'movie_name':['Bahubali','Tiger','Judwa','MS Dhoni','Tubelight'], 'movie_ratings':[4,4,3,5,3.5]}
>>> s = pd.Series(dataset)
>>> s
movie_name       [Bahubali, Tiger, Judwa, MS Dhoni, Tubelight]
movie_ratings                                [4, 4, 3, 5, 3.5]
dtype: object
>>> print(s)
movie_name       [Bahubali, Tiger, Judwa, MS Dhoni, Tubelight]
movie_ratings                                [4, 4, 3, 5, 3.5]
dtype: object
>>> s = pd.DataFrame(dataset)
>>> s
  movie_name  movie_ratings
0   Bahubali            4.0
1      Tiger            4.0
2      Judwa            3.0
3   MS Dhoni            5.0
4  Tubelight            3.5
>>> 
