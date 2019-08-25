'''
Created on Aug 24, 2019

@author: itap_testbench_02
'''
import numpy as np
import pandas as pd

from pandas import Series,DataFrame

s = Series(np.random.randint(0, 150, size = 100), index = np.arange(10,110), dtype=np.int16, name = 'Python')
print(s) 
#print(s[0])
print(s[[10,20]])
print(s[10:20])     # why starts from 20?

print(s[::2])             # ::2 what is the values from?  ===get data from 10 to 110 every 2 items
print(s[::-2])            # descending
print(s.loc[[10,20]])

######
print(s.index)
print(s.iloc[0])  # iloc index from 0 to end automatically
