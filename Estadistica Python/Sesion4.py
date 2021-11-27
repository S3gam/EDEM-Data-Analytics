

import os                              #sistema operativo
import pandas as pd                    #gestionar dataframes
import numpy as np                     #numeric python vectores
import matplotlib.pyplot as plt        #graficos

os.chdir(r'C:\Users\Chemagdlc\Desktop\Chema\EDEM\estadisticaPython\01_Sesiones\Sesion4')
os.getcwd()

wbr = pd.read_csv ('/Users/Sergi/Desktop/EDEM/Estadistica Python', sep=';',decimal = '.')



#SELECCIONAR VARIABLES que quieres conservar
my_vars=['temp_celsius','cnt']                                                  #definimos los nobres de las columnas

wbr_minimal=wbr[my_vars]                                                         #Creamos el nuevo data frame
wbr_minimal.shape
#QC OK

#SELECCIONAR CASOS

#1 explore year/ Estudio Nominal
mytable = wbr.groupby(['yr']).size()                   #tamaño de los grupos
print(mytable)

#Porcentages
n=mytable.sum()
mytable2=(mytable/n)*100
print(mytable2)

#Excursus to operators in Python

#Subset year 0 (Año 0 es el 2011)
wbr_2011 = wbr[wbr.yr == 0] #Nuevo data set en el que aparezcan solo datos del año 2011 (yr==0)

plt.hist(wbr_2011.cnt)      #grafica plot
wbr_2011.cnt.describe()


#Ejercicio 1: Dataset que aparezcan las filas donde el año sea 2012 y la estacion invierno
wbr_2012_winter = wbr[(wbr.yr == 1) & (wbr.season == 1)] #subsetting with 2 settings (importante los parentesis para operadores)
wbr_2012_winter.shape


plt.hist(wbr_2012_winter.cnt)  #Grafica plot count
plt.title("Rentals in Winter 2012")   #Titulo grafica  
wbr_2012_winter.cnt.describe()  #Datos estadisticos para valor contatitativo

#Ejercicio 2: Dataset donde aparexcan las filas donde la estacion es invierno o verano

wbr_fall_winter = wbr[(wbr.season == 1) | (wbr.season == 4)] #subsetting con 2 settings
wbr_fall_winter.shape

plt.hist(wbr_fall_winter.cnt) #grafico plot count
wbr_fall_winter.cnt.describe()


#Ejercicio 
reset -f

os.chdir(r'C:\Users\Chemagdlc\Desktop\Chema\EDEM\estadisticaPython\01_Sesiones\Sesion4')
os.getcwd()

wbr_ue = pd.read_csv ('wbr_ue.csv', sep=';',decimal = ',')

wbr_ue.temp_celsius.describe()

wbr_ue['temp_celsius_c'] = wbr_ue.temp_celsius.replace(99,np.nan)
wbr_ue.temp_celsius_c.describe()
plt.hist(wbr_ue.temp_celsius_c)

wbr_ue.temp_celsius_c.dropna() #Limpiar datos extraños/Quitar las filas que tienen nan
plt.hist(wbr_ue.temp_celsius_c.dropna())


#dropna de todo el dataset

wbr_ue2 = wbr_ue.dropna() #Solo se utiliza cuando vayas a utilizar todas las columnas



