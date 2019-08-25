'''
Created on Aug 25, 2019

@author: itap_testbench_02
'''
import numpy as np
import pandas as pd

from pandas import Series,DataFrame

df = DataFrame(np.random.randint(0,150,size = (100, 5)),index = np.arange(100,200),columns = ['Python', 'En','Math','Physic','Chem'])
#print(df)

#print(df.isnull().any())  # why is there null 129~170

#print(df.notnull().all())     

for i in range(50):
    index = np.random.randint(100,200,size = 1)[0]
    
    cols = df.columns
    
    col = np.random.choice(cols)
    
    df.loc[index,col] = None
    
for i in range(20):
    index = np.random.randint(100, 200, size = 1)[0]
    
    cols = df.columns
    
    col = np.random.choice(cols)
    
    df.loc[index, col] = np.NaN
    
print(df)    