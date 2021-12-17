

import os                                                   #Sistema operativo
import pandas as pd                                         #Gestionar dataframes
import numpy as np                                          #Numeric python vectores
import matplotlib.pyplot as plt                             #Graficos

os.chdir(r'/Users/Sergi/Desktop/EDEM/Estadistica Python')
os.getcwd()

rentals_weather_11_12 = pd.read_csv ('rentals_weather_2012.csv', sep=',',decimal = '.')


wbr = rentals_weather_11_12
del wbr['Unnamed: 0']
del(rentals_weather_11_12)



mytable = wbr.groupby(['weathersit']).size()                   #tamaño de los grupos
print(mytable)

#Porcentages
n=mytable.sum()
mytable2=(mytable/n)*100
print(mytable2)

mytable3 = round(mytable2,1)
mytable3

#Graphically
#Barchart
plt.bar(mytable2.index, mytable2)

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
#Guardar figuras
plt.savefig('bar1.eps')                                       #Guarda en formato editable
plt.savefig('bar1.jpg')                                       #Guarda en formato imagen jpg
plt.savefig('bar1.svg')                                       #Guarda en formato imagen svg
plt.show()







