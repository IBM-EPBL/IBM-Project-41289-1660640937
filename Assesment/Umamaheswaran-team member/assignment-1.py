# -*- coding: utf-8 -*-
"""Assignment_1 (1).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1XzC9ruHRmzWY8-RXlJTHHXOyHkraZr72

# Basic Python

## 1. Split this string
"""

s = "Hi there Sam!"

string = "Hi there Sam!"
print(string.split())

"""## 2. Use .format() to print the following string. 

### Output should be: The diameter of Earth is 12742 kilometers.
"""

planet = "Earth"
diameter = 12742

planet = "Earth"
diameter = 12742

print("The diameter of {} is {} kilometers.".format(planet, diameter))

#or, you can do it like that:

print(f"The diameter of {planet} is {diameter} kilometers.")

"""## 3. In this nest dictionary grab the word "hello"
"""

d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}

print(d['k1'][3]["tricky"][3]['target'][3])

"""# Numpy"""

import numpy as np

"""## 4.1 Create an array of 10 zeros? 
## 4.2 Create an array of 10 fives?
"""

import numpy as np
array=np.zeros(10)
print("An array of 10 zeros:")
print(array)

import numpy as np
array=np.ones(10)*5
print("An array of 10 fives:")
print(array)

"""## 5. Create an array of all the even integers from 20 to 35"""

import numpy as np
array=np.arange(20,36,2)
print("Array of all the even integers from 20 to 35")
print(array)

"""## 6. Create a 3x3 matrix with values ranging from 0 to 8"""

import numpy as np
x =  np.arange(2, 11).reshape(3,3)
print(x)

"""## 7. Concatenate a and b 
## a = np.array([1, 2, 3]), b = np.array([4, 5, 6])
"""

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

gfg = np.concatenate((a, b), axis = 0)
print(gfg)

"""# Pandas

## 8. Create a dataframe with 3 rows and 2 columns
"""

import pandas as pd

df = pd.DataFrame()
print(df)

"""## 9. Generate the series of dates from 1st Jan, 2023 to 10th Feb, 2023"""

import pandas as pd
per1 = pd.date_range(start ='1-1-2018', 
         end ='1-05-2018', freq ='5H')
  
for val in per1:
    print(val)

"""## 10. Create 2D list to DataFrame

lists = [[1, 'aaa', 22],
         [2, 'bbb', 25],
         [3, 'ccc', 24]]
"""

lists = [[1, 'aaa', 22], [2, 'bbb', 25], [3, 'ccc', 24]]

import pandas as pd

df = pd.DataFrame(lists, columns = ['Name', 'Age','No'])
print(df)