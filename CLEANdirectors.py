# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 22:21:58 2017

@author: Farah Jasim
"""
from openpyxl import Workbook
import xlsxwriter
import xlrd
import json
import ast
import pandas as pd
from numpy import *
from pylab import *   
file_location = 'D:/IMDb_dataset2/directors2.list.xlsx';


wd = xlrd.open_workbook(file_location)
wr = xlsxwriter.Workbook(file_location)

worksheet = wd.sheet_by_name('directors2')
worksheet1 = wr.add_worksheet()



col0_director_name = 0
col1_movie_name = 1

# tronsform the workbook to a list of dictionnary
data =[]
i = 0
row = 0
#read from the first row
str1 = worksheet.cell_value(row,col0_director_name)
str2 = worksheet.cell_value(row,col1_movie_name)

worksheet1.write(row, 0,str1)
worksheet1.write(row, 1,str2)
j = 1
for row in range(1, worksheet.nrows):
    data = 'str'
    #rad from the second row and so on
    str3 = worksheet.cell_value(row,col0_director_name)
    str4 = worksheet.cell_value(row,col1_movie_name)
    if not str3 and not str4:
        #str1 = worksheet.cell_value(row+1,col0_director_name)
        j = j
    elif not str3:
        worksheet1.write(j, 0,str1)
        worksheet1.write(j, 1,str4)
        j=j+1
    else:
        worksheet1.write(j, 0,str3)
        worksheet1.write(j, 1,str4)
        str1 = str3
        j=j+1
