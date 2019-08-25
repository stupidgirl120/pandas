'''
Created on Aug 17, 2019

@author: itap_testbench_02
'''
import pandas as pd

df = pd.read_excel('Travel Cities and Countries.xlsx')

#print(file)
print(df.iloc[0:2])
# 

for index, row in df.iterrows():
    print(index, row['Name'])
    df.decribe()
    
    df.sort_values('Name', ascending = False)
    df['Total'] = df['HP']+df['Attack']
    df['Tatal'] = df.iloc[:, 4:10].sum(axis=1)
    df = df.[['Total', 'HP', 'Defense' ]]