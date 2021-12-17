#SUSTITUIR DATOS

#########################################
import os
import numpy as np
import pandas as pd
from pandas.api.types import CategoricalDtype #For definition of custom categorical data types (ordinal if necesary)
import matplotlib.pyplot as plt
import seaborn as sns  # For hi level, Pandas oriented, graphics
import scipy.stats as stats  # For statistical inference 


wbr = pd.read_csv('WBR_11_12_denormalized_temp.csv', sep=';', decimal=',')
print(wbr.shape)
print(wbr.head())
print(wbr.info())


################################################

# Reset para borrar dataframes, variables etc.

reset -f


#################################################
# Analiza QUANTITATIVE variables agains QUANTITATIVE variables QUANTI/QUANTI
## CORRELACIÓN Y REGRESIÓN

# We will analyse if there is a realtion between the Temperature and the rentals

# 1.- Describe Variables

#### DESCRIBIMOS LA VARIABLE PRINCIPAL / cnt

## OPCIÓN CHUNGA
#histogram ver4

res = wbr.cnt.describe()
print (res)
# Store parameters as numbers
m  = res[1]
sd = res[2]
n  = res[0]

x=wbr['cnt']
plt.hist(x, bins=10, edgecolor='red')
plt.xticks(np.arange(0, 10000, step=1000))
plt.title('Figure 1. Daily Bicycle rentals in Washington DC''\n' 'by Capital bikeshare. 2011 - 2012')
plt.ylabel('Frecuency')
plt.xlabel('Number of rented bicycles')
props = dict(boxstyle='round', facecolor='white', lw=0.5)
textstr = '$\mathrm{n}=%.0f$'%(n)
plt.text (-50,128, textstr , bbox=props)


# Add reference lines and store their names in label for later legend
plt.axvline(x=m,linewidth=1,linestyle= 'solid',color="red", label='Mean')
plt.axvline(x=m-sd,linewidth=1,linestyle= 'dashed',color="green", label='- 1 S.D.')
plt.axvline(x=m + sd,linewidth=1,linestyle= 'dashed',color="green", label='+ 1 S.D.')
plt. legend(loc='upper left', bbox_to_anchor=(0.73, 0.98))


##### DESCRIBIMOS LA VARIABLE TEMPERATURA / cnt

## OPCIÓN CHUNGA
#histogram ver4

res2 = wbr.temp_celsius.describe()
print (res2)
# Store parameters as numbers
m  = res2[1]
sd = res2[2]
n  = res2[0]

x=wbr['temp_celsius']
plt.hist(x, bins=10, edgecolor='black')
plt.xticks(np.arange(0, 50, step=10))
plt.title('Figure 2. Daily Temperature in Washington DC''\n' 'by Capital bikeshare. 2011 - 2012')
plt.ylabel('Frecuency')
plt.xlabel('Temperature in Cº')
props = dict(boxstyle='round', facecolor='white', lw=0.5)
textstr = '$\mathrm{n}=%.0f$'%(n)
plt.text (1,80, textstr , bbox=props)


# Add reference lines and store their names in label for later legend
plt.axvline(x=m,linewidth=1,linestyle= 'solid',color="red", label='Mean')
plt.axvline(x=m-sd,linewidth=1,linestyle= 'dashed',color="green", label='- 1 S.D.')
plt.axvline(x=m + sd,linewidth=1,linestyle= 'dashed',color="green", label='+ 1 S.D.')
plt. legend(loc='upper left', bbox_to_anchor=(0.73, 0.98))

######

#OPCION EASY
plt.hist(x, edgecolor='black') #Easy way to plot histogram

######

## Hacemos un SCATTERPLOT para ver gráficamente si podrían estar relacionadas
 # en un Scatterplot, ponemos en el eje "x" la variable predictora y en el eje "y" la variable target
x = wbr.temp_celsius #Variable Predictora
y = wbr.cnt # Variable Target
tit = "Figure 9. Daily bicyvle rentals, by temperature"
plt.figure(figsize=(5,5))
plt.scatter(x, y, s=20, facecolor='none', edgecolors= 'C0') # La "s" significa size de los circulos
plt.ylabel('Daily rentals')
plt.xlabel('Temperature centigrades')
plt.title(tit)
plt.show()

# Correlacion de Pearson.
# La correlación de pearson indica la relación que tienen las variables, y va de -1 a 1.
# -1 sería relación inversa y 1 sería relación directa

## Importamos librería

from scipy.stats.stats import pearsonr
print(pearsonr(x, y)) #el primer num ese el coeficiente de correlacion (entre-1 y 1) y el segundo numero es el p valor
# Ya hemos hecho las variables antes


# Queremos poner los resultados numéricos en el gráfico, la n, el pvalue y la correlación de Pearson
r, pvalue = pearsonr(x, y) #almaceno cada resultado en una variable, la r guardará el primer resultado y pvalue guardará el segundo
n = len(wbr.cnt)
print('r:', round(r,3), 'pvalue:', round(pvalue,3), 'n:', n)

#incluimos los resultados de pearson en el gráfico
plt.figure(figsize=(5,5))
plt.scatter(x, y, s=20, facecolor='none', edgecolors= 'C0')
# plt.xticks(np.arrange(0,40,step=5))
# plt.yticks(np.arrange(0,10000, step=1000)) no se porque cuando activo estas dos funciones, se me borran los títulos
plt.ylabel('Daily rentals')
plt.xlabel('Temperature centigrades')
props= dict(boxstyle='round', facecolor='white', lw=0.5)
textstr = '$\mathrm{r}=%.2f$\n$\mathrm{P.Val:}=%.3f$\n$\mathrm{n}=%.0f$'%(r, pvalue, n)
plt.text (3,7000, textstr , bbox=props)
plt.title(tit)
plt.show()


#nos damos cuenta de que las bolitas forman dos capas, como dos delfines
#deducimos que podrían ser dos años distintos 2011 y 2012
#hacemos un nuevo gráfico pa que me lo dibuje por años
plt.figure(figsize=(5,5))
plt.scatter(x, y, s=20, facecolor='none', c=wbr.yr) # Hemos modificado "edgecolor" por la c, es decir ahora distinguimos los colores según el año
plt.ylabel('Daily rentals')
plt.xlabel('Temperature centigrades')
props= dict(boxstyle='round', facecolor='white', lw=0.5)
textstr = '$\mathrm{r}=%.2f$\n$\mathrm{P.Val:}=%.3f$\n$\mathrm{n}=%.0f$'%(r, pvalue, n)
plt.text (3,7000, textstr , bbox=props)

#sabiendo lo anterior, podríamos pensar que tb hay diferencias entre las estaciones
#intro gráfico
#nos damos cuenta de que este gráfico es una mierda y makes no sense
#la propia temperatura implica las estaciones, asi que distribuye los datos de una manera que no nos interesa :)
plt.figure(figsize=(5,5))
plt.scatter(x, y, s=20, facecolor='none', c=wbr.season) # Hemos utilizado otra variable para el análisis
plt.ylabel('Daily rentals')
plt.xlabel('Temperature centigrades')
props= dict(boxstyle='round', facecolor='white', lw=0.5)
textstr = '$\mathrm{r}=%.2f$\n$\mathrm{P.Val:}=%.3f$\n$\mathrm{n}=%.0f$'%(r, pvalue, n)
plt.text (3,7000, textstr , bbox=props)
# En este caso, las seasons no nos ayuda a entender mejor la correlación entre las dos variables




