
#Subsetting 


import os                              #sistema operativo
import pandas as pd                    #gestionar dataframes
import numpy as np                     #numeric python vectores
import matplotlib.pyplot as plt        #graficos

os.chdir('C:/Users/Nitropc/Desktop/MDA/Estadistica en Python/data_1_3')
os.getcwd()


# Load data

wbr = pd.read_csv('WBR_11_12_denormalized_temp.csv', sep = ";", decimal = ",")
wbr.shape
print(wbr.tail())

plt.hist(wbr.cnt)


##############################################################
#Subsetting II Selecting Variables

# 1 - Definir las variables que queremos conservar

my_vars=["temp_celsius","cnt"]  # Estas son las variables que hemos seleccionado. cnt es la cantidad alquilada de bicis,
# Vamos a ver si la temperatura en celsius es importante para la cantidad

# Extract those variables and save them into wbr_minimal

wbr_minimal=wbr[my_vars] # Le estamos dando a wbr el valor de wbr solo de las variables que hemos determinado en my_vars
wbr_minimal.shape


##############################################################
#Subsetting I Selecting cases

# Select a subsample from our data
# Select cases only from 2011
# Create a new dataframe containing observations from 2011
#Explore years / seleccionar año, variable nominal

mytable = wbr.groupby(["yr"]).size() # Esto nos devuelve el tamaño de los grupos
print(mytable)

# We are going to select only cases from year 11
#subset year 0
wbr_2011 = wbr[wbr.yr == 0]

plt.hist(wbr_2011.cnt)      #grafica plot
wbr_2011.cnt.describe()     # Nos devuelve la estadística

###########
#Ejercicio 1: Dataset que aparezcan las filas donde el año sea 2012 y la estacion invierno

wbr_2012_winter = wbr[(wbr.yr ==1) & (wbr.season == 1)]
wbr_2012_winter.shape

plt.hist(wbr_2012_winter.cnt)      #grafica plot
plt.title("Rentals in winter 2012")  #Titulo de la gráfica
wbr_2012_winter.cnt.describe()      #Datos estadisticos para valor contatitativo

##########

#Ejercicio 2: Dataset donde aparezcan las filas donde la estacion es invierno o verano

wbr_fall_winter = wbr[(wbr.season ==1) | (wbr.season == 4)]
wbr_fall_winter.shape

mytable = wbr_fall_winter.groupby(["season"]).size() # Descripción numérica
print(mytable)

wbr_fall_winter.cnt.hist()


plt.hist(wbr_fall_winter.cnt)
plt.title("Rentals in winter and fall")
wbr_fall_winter.cnt.describe()

#########

#Ejercicio EXTRA
# Sacar la media y la standard deviation

reset -f

os.chdir("C:/Users/Nitropc/Desktop/MDA/Estadistica en Python/data_1_3")
os.getcwd()

# Leer los datos
wbr = pd.read_csv('wbr_ue.csv', sep = ";", decimal = ",")
wbr.shape
print(wbr.head())

wbr.temp_celsius.describe() # Nos desribe las stats de la variable "temp_celsius" del dataframe wbr

plt.hist(wbr.temp_celsius) # Hacemos el histograma para ver si sale todo bien
# Vemos que hay datos irreales y los reemplazamos

wbr['temp_celsius_c'] = wbr.temp_celsius.replace(99,np.nan) # Creamos una nueva variable (columna)
#en la que reemplazamos el dato irreal con el "nan" que nos informa que no hay datos
wbr.temp_celsius_c.describe()
plt.hist(wbr.temp_celsius_c)



wbr.temp_celsius_c.dropna() #Limpiar datos extraños/Quitar las filas que tienen nan

plt.hist(wbr.temp_celsius_c.dropna())


#dropna de todo el dataset

wbr2 = wbr.dropna() #Solo se utiliza cuando vayas a utilizar todas las columnas
wbr2.shape



