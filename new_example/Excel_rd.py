'''
Created on Aug 17, 2019

@author: itap_testbench_02
'''
import xlrd

Excelsheet1 = "Travel Cities and Countries.xlsx"

Book1 = xlrd.open_workbook(Excelsheet1)  
#Book2 = xlrd.open_workbook(Excelsheet2)

first_sheet = Book1.sheet_by_index(0)  # it begins index(0)
#second_sheet = Book2.sheet_by_index(0)

print(first_sheet.row_values(0))

#Headings = first_sheet.row_values(0) # another way to print all values in 1st row 

#Column2Heading = Headings[2]     #pull out second column out
#print(Column2Heading)

i = 0
total = 0 

for row in range(first_sheet.nrows):
    if str(first_sheet.cell(row,1).value) == "Argentina":
        i = i + 1
#       total = total + (first_sheet.cell(row,2).value)
    else:
        pass
"""  
for row in range(second_sheet.nrows):
    if str(first_sheet.cell(row,1).value) == "Argentina":
        i = i + 1
        total = total + (second_sheet.cell(row,2).value)
    else:
        pass
"""
print(i)
