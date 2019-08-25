'''
Created on Aug 16, 2019

@author: itap_testbench_02
'''
 
import numpy as np     # numpy history and function google
import pandas as pd

from pandas import Series,DataFrame

#create
#Series is one-dimension data

s = Series(data = [120, 136, 128, 99], index = ['Math', 'python','En','Chinese'])

print(s)

print(s.shape)

v = s.values
print(v)

print(type(s.mean()))

# DataFrame is two dimension data
# similar with excel

df = DataFrame(data = np.random.randint(0,150,size = (11,3)), index = list('abcdefjhijk'), columns = ['Python','En','Math'])
print(df)   # ValueError: Shape of passed values is (10, 3), indices imply (11, 3)
print(df.shape)