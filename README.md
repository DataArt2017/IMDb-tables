# IMDb-tables
ratingDirectorsGenres table

Table that combines three features extracted from the big data set of IMDb avaiable in:
ftp://ftp.funet.fi/pub/mirrors/ftp.imdb.com/pub/temporaryaccess/

-- rating includes the rate and count(how many rate this movie)

-- Directors, I have cleaned the whole table of this feacture by writeing a code in python beacuse if we take only few rows 
that may reduce the total rows in the combined tables to a very small number because the probability of the missing movie direcector 
depends on that ...
--genres: unlike the main data table, it saperate the geners type into columns- this could be changed later according to the algorthm needs

NOW, when I tried to combine the results of two data set, it give me 261 rows, so disappointing, I was thinking first because I am connecting via the movie title and this may me not clean 
but later I found it is obvious because the orginal tables was have around 80 000 movies and that been reduced when I combined these tables to 56 396 rows(movies)
the nuumber hase reduced because the data is not complete and there is for example movies do not exit in the director table an so on.

I am think now to add the diector column to the main data (TMDb 5000 data set) this generate a data set then join the data available as attached 
so the aim to increase the number of samples(row, movies) rather collect the feactures from different data set.


the SQL code for joining only the rate and directors tables are:

/****** Script for SelectTopNRows command from SSMS  ******/
SELECT R.[id]
--      ,R.[episode_title]
--      ,R.[kind]
      ,R.[rating_rank]
      ,R.[rating_votes]
      ,R.[title]
	  ,D.[directorName]
  FROM [IMBb_Final].[dbo].[ratings] AS R, 
  [IMBb_Final].[dbo].[directors_cleaned_modified3] AS D
  WHERE D.movieId = R.id
  AND R.kind ='movie'
  
  the SQL code for joining the rate, genres and directors tables are:
  
  
/****** Script for SelectTopNRows command from SSMS  ******/
SELECT R.[id]
--      ,R.[episode_title]
--      ,R.[kind]
      ,R.[rating_rank]
      ,R.[rating_votes]
      ,R.[title]
	  ,D.[directorName]
	  ,G.genres_0, G.genres_1,G.genres_2,G.genres_3,G.genres_4,G.genres_5,G.genres_6,G.genres_7,G.genres_8,
	  G.genres_9,G.genres_10,G.genres_11,G.genres_12,G.genres_13,G.genres_14
  FROM [IMBb_Final].[dbo].[ratings] AS R, 
  [IMBb_Final].[dbo].[directors_cleaned_modified3] AS D,
  [IMBb_Final].[dbo].[genres] as G
  WHERE D.movieId = R.id
  AND R.id = G.id
  AND R.kind ='movie'
  
  Python code for cleaning and ajusting director table:# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 22:21:58 2017

@author: Faraj Jasim
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
#file_location2 = 'C:/Users/haide/Desktop/datafoundation/Group Coursework/Data set/IMDb_movies_write.xlsx';


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


Farah Jasim

 
