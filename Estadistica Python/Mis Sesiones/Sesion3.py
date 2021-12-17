
import os                                                   #Sistema operativo
import pandas as pd                                         #Gestionar dataframes
import numpy as np                                          #Numeric python vectores
import matplotlib.pyplot as plt                             #Graficos

os.chdir('C:/Users/Nitropc/Desktop/MDA/Estadistica en Python/data_1_3')
os.getcwd()

# Tenemos que arreglar los csv para poder unirlos

bikes2011 = pd.merge(weather_2011, rentals_2011, on = "day")
bikes2012 = pd.read_csv("rentals_weather_2012.csv", sep=';', decimal=',')
del bikes2011["dteday_y"]
bikes2011 = bikes2011.rename(columns = {"dteday_x": "dteday"})

bikes2012.shape
bikes2011.shape


# Merge both dataframes:

bikes11_12 = bikes2011.append(bikes2012, ignore_index=True)


wbr = bikes11_12

#Create a dataframe with the table of frequencies

mytable = wbr.groupby(['weathersit']).size()
print(mytable)

# Transform frequencies to percentages
# a) obtain n ()
n=mytable.sum()

mytable2=(mytable/n)* # b) divide by n in order to get proportions,and multiply by 100

print(mytable2)


# Round to your pleasure
mytable3=round(mytable2,1)
print(mytable3)

# GRAPHICALLY:
# Barchart Nominal Values

barlist = ['Sunny', 'Cloudy', 'Rainy'] #Definimos qué representa las barras del gráfico
plt.bar(barlist,mytable2)
plt.ylabel("Percentage") # Modificamos el nombre del eje Y

# Other modifications

plt.title("Figure 1. Percentage of weather situations")
plt.text(1.85,50,'n: 731') #El interior de lo que sale en la caja
props = dict(boxstyle='round', facecolor='white',lw=0.5) # diseño de la caja
textstr = '$\mathrm{n}=%.0f$'%(n) 
plt.text (1.85,50, textstr , bbox=props)

#Guardar figuras

plt.savefig('bar1.eps')  #editable en Adobe Illustrator
plt.savefig('bar2.jpg')  #imagen tipo foto (no editable)
plt.savefig('bar.svg')   #formato vectorial: si le das zoom no se pixela

##################################################################################

#Quantitative values historygram

rentals_2011.cnt                          
np.mean(rentals_2011.cnt)                               #Media
np.std(rentals_2011.cnt)                                #Desviacion tipica

rentals_2011.cnt.describe()                             #Descripcion estadistica



#histograma

plt.hist(rentals_2011.cnt)
rentals_2011.cnt.hist() 

#histogram ver4


res = wbr.cnt.describe()
print (res)
# Store parameters as numbers
m  = res[1]
sd = res[2]
n  = res[0]


plt.hist(x, bins=10, edgecolor='black')
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

#Plot
x=rentals_2011.cnt                                      #Cuando la variable no tiene cosas extrañas (espacios, puntos...)
x=rentals_2011['cnt']                                   #Es mas robusta (no tiene en cuenta espacions, puntos...)



plt.hist(x, edgecolor='black')                          #Cambia color bordes del histograma
plt.xticks(np.arange(0, 8000, step=1000))              #Define los valores del eje x
plt.title("Figure1.  Registeres rentals in Washintong") #Titulo de la tablla
plt.ylabel("Frecuency")                                #Pone nombre al eje y
plt.xlabel("Number of rentals")                         #Pone nombre al eje x
# plt.show()                                             #Cierra el grafico

# Add reference lines and store their names in label for later legend
plt.axvline(x=4504,
linewidth=1,
linestyle= 'solid',
color="red", label='Mean')


###################################################################################

#Boxplot
plt.boxplot(x,patch_artist=True,
vert=False,
labels=['# rentals'])
plt.xticks(np.arange(0, 10000, step=1000))
plt.show()


