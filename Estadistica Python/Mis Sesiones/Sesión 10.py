#SUSTITUIR DATOS

#########################################
import os
import numpy as np
import pandas as pd
from pandas.api.types import CategoricalDtype #For definition of custom categorical data types (ordinal if necesary)
import matplotlib.pyplot as plt
import seaborn as sns  # For hi level, Pandas oriented, graphics
import scipy.stats as stats  # For statistical inference 

os.chdir('/Users/Sergi/Desktop/EDEM/EDEM-Data-Analytics/Estadistica Python/Ejercicios Chema')
os.getcwd()





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

print(model1B.summary2()) # El summary 2 es el que usamos normalmente, por tanto es lo que usamos por defecto para la regresión


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

from stargazer.stargazer import Stargazer

stargazer = Stargazer([model1,model2,model3])
stargazer.render_html() # Esto nos hace una imagen render en html, luego tenemos que coger lo que nos da y
 # Ponerlo en un lector html para ver el resultado
 # Esto nos dará también un " adjusted R square " que es básicamente una R square pero ajustada teniendo en cuenta
    # el resto de variable
 # Esto de tener en cuenta el resto de variables se llama ceteris paribus - mantener constante el resto de variables
 
###################
# Meter variables qualitativas de más de 2 valores
  # Tendremos que crear un sistema dumies que creará difrentes variables para cada una de las opciones
  
dummies = pd.get_dummies(wbr.weathersit)
colnames = {1:"sunny",2:"cloudy",3:"rainy"} # Aquí estamos relacionando el valor de la variable weathersit con la nueva etiqueta de variable
dummies.rename(columns= colnames, inplace = True)
wbr = pd.concat([wbr,dummies], axis=1)
 # Esto nos crea 3 variables una para cada valor
 
# METEMOS LAS VARIABLES EN EL MODELO
 # NO podemos meter todas las varibles que hemos creado, tenemos que dejar una fuera
 
model6 = ols("cnt ~ windspeed_kh + temp_celsius + hum + yr + cloudy + workingday + rainy",data=wbr).fit() # Hemos añadido las variables cloudy y rainy, nos dejamos fuera sunny
     # Nos dejamos fuera la variable que más se repita en este caso, lo tipico es que haga sol, por tanto dejamos fuera la variable "sunny"
     # Dejar fuera la variable modal (que es la que más se repite) ayuda a la interpretación
model6.summary2()
# Intercept es el punto de partida cuando el resto de variables es 0
# El intercept + el Coef de cada variable nos da el punto de partida para dicha variable
    # Por ejemplo, Si el dia es Rainy, el punto de partida sería el intercept - el coef. de rainy (1721.1827 + (-1786.9919))
        # Como hemos dejado fuera el sunny, el intercept es para los dias sunny, por tanto los dias cloudy se venden 478.8891 MENOS que en los sunny, y los rainy se venden 1786.9919 MENOS que en los sunny
#######################
# Off road regresion
m=4500
print(m)
wbr.loc[ (wbr['cnt']<m), "goal"]=0
wbr.loc[ (wbr['cnt']>=m), "goal"]=1

plt.scatter(wbr.cnt, wbr.goal) # Eso tes el quality control para ver que hemos hecho bien la particion

wbr.goal.hist() # Aquí vemos cuantos dias estamos por encima del goal y cuantos debajo


##########################

# Coeficientes de regresión logística - Cuando la variable dependiente (o variable target) es CUALITATIVA

from statsmodels.formula.api import logit


model1_l1 = logit('goal ~ temp_celsius', data=wbr).fit() # goal es la variable dependiente o variable target, y temp_celsius la variable modificadora
print(model1_l1.summary2())


model1_l7 = logit('goal ~ temp_celsius + hum + yr + cloudy + workingday + rainy', data=wbr).fit() 
print(model1_l7.summary2())
 # En los coeficientes tenemos que fijarnos si es positivo o negativo y si es relevante (mirando el pvalue)
 # Cuando augmenta la variable X, la probabilidad de que las ventas sean altas (augmenta si es positivo)(Disminuye si es negativo)


##########################
# Cuando hacemos un modelo lineal, es mejor sacar el cuadrado de la variable porque possiblemente sea más accurate
# Hacemos ajuste al cuadrado

# 1 - Creamos la variable al cuadrado
wbr["temp2"]= wbr.temp_celsius*wbr.temp_celsius
  
# 2 Creamos el modelo con la temp al cuadrado

model7 = ols("cnt ~ windspeed_kh + temp2 + hum + yr + workingday",data=wbr).fit()
model7.summary2()
# El coeficiente al cuadrado modula la linea de la variable en los valores altos de la variable








