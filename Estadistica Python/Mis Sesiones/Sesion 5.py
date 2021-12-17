# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 15:52:50 2021

@author: Nitropc
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 19:14:00 2021

@author: rafap
"""

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas.api.types import CategoricalDtype

os.getcwd()


os.chdir('C:/Users/Nitropc/Desktop/MDA/Estadistica en Python/data_1_3')
os.getcwd()

wbr =pd.read_csv('WBR_11_12_denormalized_temp.csv', sep=';', decimal= ',')

#Define a list with the subset of variables I want to extract
my_vars =['temp_celsius', 'cnt']

wbr_minimal= wbr[my_vars]

wbr_minimal.shape

#Select a subsample from our data
#Select cases only from 2011
#Explore years


mytable = wbr.groupby(['yr']).size()
print(mytable)

n = mytable.sum()
mytable2= (mytable/n)*100
print(mytable2)


#Subset year 0
wbr_2011 = wbr[wbr.yr==0]
plt.hist(wbr_2011.cnt)
wbr_2011.cnt.describe()
x = wbr_2011.cnt
plt.hist(x, bins=10,edgecolor='black')

#Exercise1a
#Make a histogram of the Bike rentals in Washington on the Winter of 2012
#Subsetting with two conditions
wbr_winter_2012 = wbr[(wbr.yr==1) & (wbr.season==1)]

wbr_winter_2012.shape
plt.hist(wbr_winter_2012.cnt)
x = wbr_winter_2012.cnt
plt.hist(x, bins=10,edgecolor='black')

wbr_winter_2012.cnt.describe()


#Exercise1b 
#Make a histogram of the Bike rentals in Washington during the Winter AND the Fall
wbr_fall_winter = wbr[(wbr.season==4) | (wbr.season==1)]

wbr_fall_winter.shape
plt.hist(wbr_fall_winter.cnt)
wbr_fall_winter.cnt.describe()



mytable = wbr_fall_winter.groupby(['season']).size()
print(mytable)

reset -f

#Exercise2
#Compute the average temperuture and the standard deviation in Washington
os.getcwd()

os.chdir('C:/Users/rafap/Desktop/EDEM/4. Fundamentos/Programación Estadística/PEP')
os.getcwd()
wbr_ue =pd.read_csv('wbr_ue.csv', sep=';', decimal= ',')

wbr_ue.temp_celsius.describe()
plt.hist(wbr_ue.temp_celsius)
#Plot your data


wbr_ue['temp_celsius_c'] = wbr_ue.temp_celsius.replace(99,np.nan) #Replacing 99 values with nan
wbr_ue.temp_celsius_c.describe()

plt.hist(wbr_ue.temp_celsius_c)#See the difference graphically

#To see columns
wbr_ue.temp_celsius
wbr_ue.temp_celsius_c.dropna() #Takes away all the nan


plt.hist(wbr_ue.temp_celsius_c.dropna())

wbr_ue2= wbr_ue.dropna() #Para depurar TODO el dataset, si lo utilizas TODO el data set

plt.hist(wbr_ue.temp_celsius_c.dropna(),edgecolor="black")
plt.savefig('temp.jpg')

##################################################################################

#TRANSFORMATIONS, session 6
#Lets compute the casual to registered rentals ratio

#Note that for creation of new columns we use “ robust ” column specification with [“”] not attribute call
wbr['cs_ratio'] = (wbr.casual)/(wbr.registered)
wbr.cs_ratio.describe()
plt.hist(wbr.cs_ratio)

#Histogram ver4
x = wbr.cs_ratio
res = wbr.cs_ratio.describe()
m= res[1]
sd= res[2]
n= res[0]

plt.hist(x, bins=10,edgecolor='black') # DAmos color al borde de las barras

del(wbr['cnt'])

#Calcular columna con suma TRANSFORMAR COLUMNA
wbr['cnt']=wbr.casual + wbr.registered

#1INV, 2PRIM, 3VER, 4OTO Recodificar season
#Hacer nueva columna transformandola
wbr.loc[(wbr['season']==1), "season_cat"]="Winter"
wbr.loc[(wbr['season']==2), "season_cat"]="Spring"
wbr.loc[(wbr['season']==3), "season_cat"]="Summer"
wbr.loc[(wbr['season']==4), "season_cat"]="Autumn"


#Quality Control
pd.crosstab(wbr.season, wbr.season_cat)
#QC OK

res=wbr['cnt'].describe()
print(res)

m= res[1]
sd= res[2]
n= res[0]


print("Lower limit: ", round((m-sd),1))
print("Upper limit: ", round((m+sd),1))


x = wbr['cnt']
plt.hist(x,bins=10, edgecolor='black')
plt.xticks

#Pasar una variable cuantitativa a ordinal
m -sd
m+sd

print('Low limit', round(m -sd,0))
print('Upper limit', round(m -sd,0))

wbr.loc[:,'cnt_cat1']="low rentals"

#Recode2

wbr.loc[(wbr['cnt']<2566), "cnt_cat2"]="1. Low Rentals"
wbr.loc[(wbr['cnt']>=2566) & (wbr['cnt']<6442), "cnt_cat2"]="2. Average Rentals"
wbr.loc[(wbr['cnt']>=6442), "cnt_cat2"]="3. High Rentals"

#Quality control 2
plt.scatter(wbr.cnt, wbr.cnt_cat2), s=1)

mytable= pd.crosstab(index=wbr["cnt_cat2"], columns="count")
print(mytable)

n=mytable.sum()


#Recoding into ordinal categories - Data Prep
# Recode the number of rentals in Three Groups
#Compute & store the cutting points

res = wbr['cnt'].describe()

m = res[1]
sd= res[2]
n = res[0]

# Recode 2

wbr.loc[ (wbr ['cnt']<(m- sd )) ,"cnt_cat3"]= "Low rentals"
wbr.loc[ ((wbr ['cnt']>(m - sd )) & (wbr['cnt']< m+sd )) ,"cnt_cat3"]= "Average rentals"
wbr.loc[ (wbr['cnt']> (m+sd )) ,"cnt_cat3"]= "High rentals"

mytable= pd.crosstab(index=wbr["cnt_cat3"], columns="count")
print(mytable)
n=mytable.sum()

mytable2=(mytable/n)*100
print(mytable2)

wbr.dtypes #Give me all the types of data on my dataframe
#Method2
# Vamos a generar una variable categorica

# Import specific functionality
from pandas.api.types import CategoricalDtype

# First define a specific categorical data type specific for us!!! (in two sub-steps)

# Step 1: declare the ordered categories
my_categories=["Low rentals", "Average rentals", "High rentals"]

#Step 2: Define new data type
my_rentals_type = CategoricalDtype(categories=my_categories, ordered=True)

# Second create a new categorical_ordered variable using our specific data type
wbr["cnt_cat5"] = wbr.cnt_cat3.astype(my_rentals_type)
#Then when you plot the variable or include it in further analyses, the categories will show up
# in your desired order


mytable = wbr.groupby(['cnt_cat5']).size()                   #tamaño de los grupos
print(mytable)

#Porcentages
n=mytable.sum()
mytable2=(mytable/n)*100
print(mytable2)

plt.bar(mytable2.index, mytable2)



