# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# Alberto Sanz.
# 2019_09_01
# Our first dataset

import pandas as pd

# Define variables.

name = ["Bianca", "Pedro", "Alberto"]
gender = ["Female","Male","Male"]
age = [20, 35, 46]

#Create a dataframe

class2019 = pd.DataFrame({"name" : name, "gender" : gender, "age" : age})


class2019.head()

# Export dataframe to excel

class2019.to_excel("class2019.xlsx")


# Reading external data in CSV

import os                                               #Sistema operativo
import pandas as pd                                     #Gestionar dataframes
import numpy as np                                      #Numeric python vectores
import matplotlib.pyplot as plt                         #Graficos

# Change working directory

os.chdir('C:/Users/Nitropc/Desktop/MDA/Estadistica en Python')
os.getcwd()

#Reads data from CSV file and stores it in a dataframe called rentals_2011
#Pay atention to the specific format of your CSV data (; , or , .)


#Vamos a meternos en la carpeta de datasets para abrir el documento que nos pide

os.chdir('C:/Users/Nitropc/Desktop/MDA/Estadistica en Python/data_1_3')
rentals_2011 = pd.read_csv("weather_washington_2011.csv", sep=";", decimal = ",")
rentals_2011.shape
rentals_2011.head() #Nos muestra en pantalla las filas y columnas del dataframe



#Datos cuantitativos

rentals_2011.cnt                          
np.mean(rentals_2011.cnt)                               #Media
np.std(rentals_2011.cnt)                                #Desviacion tipica

rentals_2011.cnt.describe()                             #Descripcion estadistica



#histograma

plt.hist(rentals_2011.cnt)
rentals_2011.cnt.hist() 


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

#Boxplot
plt.boxplot(x,patch_artist=True,
vert=False,
labels=['# rentals'])
plt.xticks(np.arange(0, 10000, step=1000))
plt.show()



# Reading external data from EXCEL


#Reads data from EXCEL and stores it in a dataframe named rentals_2011
rentals_2011 = pd.read_excel ("washington_bike_rentals_2011.xlsx")
rentals_2011.shape
rentals_2011.head()



# Expanding the dataset
#Load weather data in a new dataframe

weather_2011 = pd.read_csv("weather_washington_2011.csv", sep=";", decimal = ',')
weather_2011.shape
weather_2011.head()

# Merge the two dataframes(rentals & weather) into a new single dataframe

rentals_weather_2011 = pd.merge(weather_2011, rentals_2011, on = 'day') # Here we are merging by using as reference the column day
rentals_weather_2011.shape
rentals_weather_2011.head()





# ADD NEW CASES(Rows) TO DATAFRAME

# Read cases from another year (2012) in a new dataframe

rentals_weather_2012 = pd.read_csv("rentals_weather_2012.csv", sep = ';', decimal= ',')
rentals_weather_2012.shape
rentals_weather_2012.head()

#Check dimensionality of both dataframes
print(rentals_weather_2011.shape)
print(rentals_weather_2012.shape)

#WE CAN MERGE THE TWO DATA FRAMES IN A NEW ONE CONTAINING SAME
#VARIABLES(COLUMNS) BUT MORE CASES(ROWS)

rentals_weather_11_12 = rentals_weather_2011.append(rentals_weather_2012, ignore_index=True) 

print (rentals_weather_11_12.shape)
print (rentals_weather_11_12.head())
print (rentals_weather_11_12.tail())



rentals_weather_11_12.to_csv("bikes2012.csv")

