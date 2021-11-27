reset -f

import os                                               #Sistema operativo
import pandas as pd                                     #Gestionar dataframes
import numpy as np                                      #Numeric python vectores
import matplotlib.pyplot as plt                         #Graficos

os.chdir(r'Users/Sergi/Desktop/EDEM/Estadistica Python')
os.getcwd()

#Reads data from CSV 
rentals_2011 = pd.read_csv ('washington_bike_rentals_2011.csv', sep=';',decimal = ',') #Lee y cambias ; por ,


rentals_2011.shape                                      #Nos da el numero de filas y las columnas
rentals_2011.head()                                     #Nos muestra las primeras filas
rentals_2011.tail()                                     #Nos muestra las ultimas
#QC OK

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
plt.xticks(np.arange(0, 10000, step=1000))              #Define los valores del eje x
plt.title("Figure1.  Registeres rentals in Washintong") #Titulo de la tablla
plt.ylabel("Frecuencia")                                #Pone nombre al eje y
plt.xlabel("Number of rentals")                         #Pone nombre al eje x
plt.show()                                              #Cierra el grafico




#Nuevo DataSet
weather_2011 = pd.read_csv ('weather_washington_2011.csv', sep=';',decimal = ',')

weather_2011.shape  
weather_2011.dtypes                                     
                                   
weather_2011.head()                                    
weather_2011.tail()  
#QC OK


# Merge the two dataframens into a new one
rentals_weather_2011 = pd.merge(weather_2011, rentals_2011, on='day')  #Fusiona las dos tablas segun la columna de dia


rentals_weather_2011.shape 

rentals_weather_2011.to_csv("rentals_weather_2011.csv") #Guardar nuevo csv


#Borrar una columna (borramos dteday_y por que esta repetida)
del rentals_weather_2011['dteday_y']
rentals_weather_2011.shape 

rentals_weather_2011 = rentals_weather_2011.rename(columns={"dteday_x":"dteday"})


#ADD NEW CASES(Rows) TO DATAFRAME: rentals_weather_2012

rentals_weather_2012 = pd.read_csv ('rentals_weather_2012.csv', sep=';',decimal = ',')

rentals_weather_2012.shape
rentals_weather_2012.head()
rentals_weather_2012.tail()
#QC OK

rentals_weather_11_12 = rentals_weather_2011.append(rentals_weather_2012) #añade por el final el dataset: rentals_weather_2012
rentals_weather_11_12.shape  
rentals_weather_11_12.to_csv("rentals_weather_11_12.csv")




