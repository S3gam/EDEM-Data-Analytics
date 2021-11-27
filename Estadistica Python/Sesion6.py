#SUSTITUIR DATOS
import os                              #sistema operativo
import pandas as pd                    #gestionar dataframes
import numpy as np                     #numeric python vectores
import matplotlib.pyplot as plt        #graficos

os.chdir(r'/Users/Sergi/Desktop/EDEM/Estadistica Python')
os.getcwd()

wbr = pd.read_csv ('WBR_11_12_denormalized_temp.csv', sep=';',decimal = ',')

### Computing new columns
wbr['cs_ratio'] = (wbr.casual)/(wbr.registered)

wbr.cs_ratio.describe()
plt.hist(wbr.cs_ratio)


del wbr['cnt']

wbr['cnt'] = wbr.casual + wbr.registered

#Recodificar una variable
##1 winter, 2 spring, 3 summer, 4 fall
###Recodificar una variavle numero por una de txt

wbr.loc[(wbr['season']==1),"season_cat"]= "Winter"                             #Crear una columna nueva donde el codigo de la columna season se asigne a un texto (estaciones)
wbr.loc[(wbr['season']==2),"season_cat"]= "Spring"
wbr.loc[(wbr['season']==3),"season_cat"]= "Summer"
wbr.loc[(wbr['season']==4),"season_cat"]= "Autum"

####Comprobar de manera sistematica que está bien (tabla cruzada)
pd.crosstab(wbr.season, wbr.season_cat)                                         #Se ve viualmente mejor si es erroneo o no mediante una matriz
     #QC OK

res = wbr['cnt'].describe()
print(res)


###Recode 1
wbr.loc[(wbr['cnt']<2566),"cnt_cat2"]= "1: Low rentals"

wbr.loc[((wbr['cnt']>=2566) & (wbr['cnt']<6442)),"cnt_cat2"]= "2: Average rentals"

wbr.loc[(wbr['cnt']>=6442),"cnt_cat2"]= "3: Hight rentals"

####♦Quality control?
plt.scatter(wbr.cnt, wbr.cnt_cat2)

mytable = wbr.groupby(['cnt_cat2']).size()                   #tamaño de los grupos
print(mytable)

#Porcentages
n=mytable.sum()
mytable2=(mytable/n)*100
print(mytable2)


plt.bar(mytable2.index, mytable2)

###Recode 2
wbr.loc[(wbr['cnt']<2566),"cnt_cat3"]= "Low rentals" #El cat3 se hace porque estamos creando otra columna diferente de datos

wbr.loc[((wbr['cnt']>=2566) & (wbr['cnt']<6442)),"cnt_cat3"]= "Average rentals"

wbr.loc[(wbr['cnt']>=6442),"cnt_cat3"]= "Hight rentals"

####♦Quality control?
plt.scatter(wbr.cnt, wbr.cnt_cat3)

mytable = wbr.groupby(['cnt_cat3']).size()                   #tamaño de los grupos
print(mytable)

#Porcentages
n=mytable.sum()
mytable2=(mytable/n)*100
print(mytable2)


plt.bar(mytable2.index, mytable2)

# Vamos a generar una variable categorica

# Import specific functionality
from pandas.api.types import CategoricalDtype

# First define a specific categorical data type specific for us!!! (in two sub-steps)

# Step 1: declare the ordered categories
my_categories=["Low rentals", "Average rentals", "Hight rentals"]

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

