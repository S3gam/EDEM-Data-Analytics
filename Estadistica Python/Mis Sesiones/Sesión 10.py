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


#######################################################

### MODELO DE REGRESIÓN
# De variable QUANTITATIVA a QUANTITATIVA

# DEFINIMOS VARIABLES como de costumbre

wbr.cnt.hist() # checkeo rápido para ver si está limpio

res2 = wbr.temp_celsius.hist()
print(res2)

# 2 - Hacer el Scatterplot

x = wbr.cnt
y = wbr.temp_celsius

plt.scatter(y, x, s=20, facecolor='none', edgecolors= 'C0') # La variable Target siempre eje Y / la variable predictora eje x 


from statsmodels.formula.api import ols


# 3 - Sacar el R-square, Intercept y pendiente

# OLS Ordinary Least Squares
model1 = ols("cnt ~ temp_celsius", data=wbr).fit() # Esto nos da la línea estadísticamente perfecta que nos reflejaría la relación entre "cnt" y "temp_celsius"
# cnt es la Target Variable y la temperarura la variable modificadora

print(model1.summary2())
# El intercept/constant que nos da es el punto de partida de la recta, es decir, el valor de la y cuando la x sea 0
# El segundo coeficiente es cuanto se incrementa la variable target por cada incremento en una unidad de la variable predictora. En este caso en la table sale "temp_celsius"
# El valor alfa es un standard autoimpuesto, mientras que el pvalue es algo que no se puede pasar

# La R-squared nos dice qué porcentage de la variabilidad de x depende de la variable y,
    # En este caso, la variabilidad de las rentals depende un 39,4% de la temperatura que haga

temp = 30
rentals = 1215 +162*temp
print(rentals)

#####################################################
# Modelo de Regresión para la velocidad del viento
# 1 - Definimos las variables

wbr.cnt.hist() # checkeo rápido para ver si está limpio

res3 = wbr.windspeed_kh.hist()
print(res3)


# 2 - Hacer el Scatterplot
xb = wbr.cnt
yb = wbr.windspeed_kh

plt.scatter(yb, xb, s=20, facecolor='none', edgecolors= 'C0') # La variable Target siempre eje Y / la variable predictora eje x 


# 3 - Sacar el R-square, Intercept y pendiente

# OLS Ordinary Least Squares
model1B = ols("cnt ~ windspeed_kh", data=wbr).fit() # Esto nos da la línea estadísticamente perfecta que nos reflejaría la relación entre "cnt" y "temp_celsius"
# cnt es la Target Variable y la temperarura la variable modificadora

print(model1B.summary2())


# Aquí hemos hecho OLS sumatoria
model2 = ols("cnt ~ windspeed_kh + temp_celsius",data=wbr).fit() # Aquí hacemos una ols de 2 variables
model2.summary2()
# Ahora los coeficientes de las variables nos diría como cambiaria una variable en el caso que las otras estubieran fijas
# 


model3 = ols("cnt ~ windspeed_kh + temp_celsius + hum",data=wbr).fit() # Aquí hacemos una ols de 3 variables
model3.summary2()


# Añadimos una variable NOMINAL / QUALITATIVA
model4 = ols("cnt ~ windspeed_kh + temp_celsius + hum + yr",data=wbr).fit() # Aquí hacemos una ols de 4 variables y una QUALITATIVA
model4.summary2()








