#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 15:30:41 2021

@author: Sergi
"""
'''

1. Describe the two variables involved in the
ypothesis
2. Perform the numeric test: t.test
3. Perform the graphic test: plot of the means
4. When posible: combine both numeric and graphic in
same plot

'''

# 0 
import os                              #sistema operativo
import pandas as pd                    #gestionar dataframes
import numpy as np                     #numeric python vectores
import matplotlib.pyplot as plt        #graficos
import scipy.stats as stats            #Libreía que se usa para hacer estadísticas

os.chdir(r'/Users/Sergi/Desktop/EDEM/Estadistica Python')
os.getcwd()

wbr = pd.read_csv ('WBR_11_12_denormalized_temp.csv', sep=';',decimal = ',')
print(wbr.shape)

# Comparacion de medias
# 1. Describir variables
import pandas as pd

wbr.cnt.describe()
plt.hist(wbr.cnt)

mytable = wbr.groupby(['workingday']).size()

n = mytable.sum()
mytable = (mytable/n)*100
barlist = ['Not Working Day', 'Working Day']
plt.bar(barlist, mytable)
plt.ylabel('Percentage')

# 2 Descriptive comparison:
    # Hacer test numérico
wbr.groupby('workingday').cnt.mean()

#Statistical comparison:
#Extract the two sub samples and store them in two objects
cnt_wd=wbr.loc[wbr.workingday==1, "cnt"]
cnt_nwd=wbr.loc[wbr.workingday==0, "cnt"] 

#Perform a t test for mean comparison
stats.ttest_ind(cnt_wd, cnt_nwd, equal_var = False) #Este test nos dice que probabilidad hay de que las diferencias de la muestra se apliquen a la realidad
# El pvalue es la probabilidad de que no haya ninguna diferencia entre los datos que estamos comparando
# Es decir, cuanto más alto sea el pvalue, más diferencias habrá
# Si el pvalue es mayor de 0.05, concluimos que estos datos no son vinculantes puesto que la probabilidad de error esdemasiado alta
# Por tanto, en este caso, el woriking day no tienen impacto real sobre las ventas



# 3 Perform the graphic test: plot of the means


import seaborn as sns

plt.figure(figsize=(5,5))

ax = sns.pointplot(x="workingday", y="cnt", data=wbr,ci=95, join=0)

# Ajustar eje y
plt.yticks(np.arange(3000, 7000, step=500))
plt.ylim(2800,6200)

# Pinyst linea en la media
plt.axhline(y=wbr.cnt.mean(),
linewidth=1,
linestyle= 'dashed',
color="red")

#Caja de texto
props = dict(boxstyle='round',
facecolor='white', lw=0.5)

#Texto ejes
plt.text(0.85,5400,'Mean:4504.3''\n''n:731' '\n' 't:1.601' '\n' 'Pval.:0.110', bbox=props)
plt.xlabel('Working Day')
plt.title('Figure 6. Average rentals by Working Day.''\n')

# CAMBIAMOS A AÑO


wbr.groupby('year').cnt.mean()

#Statistical comparison:
#Extract the two sub samples and store them in two objects
cnt_wd=wbr.loc[wbr.yr==1, "cnt"]
cnt_nwd=wbr.loc[wbr.yr==0, "cnt"] 

#Perform a t test for mean comparison
stats.ttest_ind(cnt_wd, cnt_nwd, equal_var = False) 

import seaborn as sns

plt.figure(figsize=(5,5))

ax = sns.pointplot(x="yr", y="cnt", data=wbr,ci=95, join=0)
plt.yticks(np.arange(3000, 7000, step=500))
plt.ylim(2800,6200)

plt.axhline(y=wbr.cnt.mean(),
linewidth=1,linestyle= 'dashed', color="red")

props = dict(boxstyle='round',
facecolor='white', lw=0.5)

plt.text(0.85,3000,'Mean:4504.3''\n''n:731' '\n' 't:18.601' '\n' 'Pval.:0.000', bbox=props)
plt.xlabel('Working Day')
plt.title('Figure 6. Average rentals by year.''\n')



# MEAN COMPARISON, comparativas de más de 2 variables slide 18

mytable = wbr.groupby(['weathersit']).size()     #tamaño de los grupos
print(mytable)

#Porcentages
n=mytable.sum()
mytable2=(mytable/n)*100
print(mytable2)

mytable3 = round(mytable2,1)
mytable3

#Graphically
#Barchart

#barchart1
#lets label the cathegories
bar_list = ['Sunny', 'Cloudy', 'Rainy']

plt.bar(bar_list, mytable2)

#Barchart2
bar_list = ['Sunny', 'Cloudy', 'Rainy']
plt.bar(bar_list, mytable2,edgecolor='black')
plt.ylabel('Percentage')
plt.title('Figure 1. Percentage of weather situations')
props = dict(boxstyle='round', facecolor='white', lw=0.5)
textstr = '$\mathrm{n}=%.0f$'%(n)
plt.text (2,60, textstr , bbox=props)



# Hacer test numérico
wbr.groupby('weathersit').cnt.mean()

#Statistical comparison:
#Extract the two sub samples and store them in two objects
cnt_sunny=wbr.loc[wbr.weathersit==1, "cnt"]
cnt_cloudy=wbr.loc[wbr.weathersit==2, "cnt"] 
cnt_rainy=wbr.loc[wbr.weathersit==3, "cnt"] 

#Perform a t test for mean comparison
stats.f_oneway(cnt_sunny, cnt_cloudy, cnt_rainy)
print (res)
print ("F:", round(res[0],3), p)


import seaborn as sns

plt.figure(figsize=(5,5))

ax = sns.pointplot(x="weathersit", y="cnt", data=wbr,ci=95, join=0)

# Ajustar eje y
plt.yticks(np.arange(0000, 7000, step=500))
plt.ylim(800,6200)

# Pinyst linea en la media
plt.axhline(y=wbr.cnt.mean(),
linewidth=1,
linestyle= 'dashed',
color="red")

#Caja de texto
props = dict(boxstyle='round',
facecolor='white', lw=0.5)

#Texto ejes
plt.text(0.85,5400,'Mean:4504.3''\n''n:731' '\n' 't:1.601' '\n' 'Pval.:0.110', bbox=props)
plt.xlabel('Weather')
plt.title('Figure 7. Average rentals by weather''\n')



