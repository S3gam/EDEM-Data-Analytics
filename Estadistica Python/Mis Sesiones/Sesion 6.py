#SUSTITUIR DATOS

#########################################
import os
import numpy as np
import pandas as pd
from pandas.api.types import CategoricalDtype #For definition of custom categorical data types (ordinal if necesary)
import matplotlib.pyplot as plt
import seaborn as sns  # For hi level, Pandas oriented, graphics
import scipy.stats as stats  # For statistical inference 


os.chdir('C:/Users/Nitropc/Desktop/MDA/Estadistica en Python/data_1_3')
os.getcwd()

################################################

# Reset para borrar dataframes, variables etc.

reset -f


#################################################

#Load data


wbr = pd.read_csv ('WBR_11_12_denormalized_temp.csv', sep=';',decimal = ',')


###################################################


#Working days CUALITATIVA en una CUANTITATIVA comparación de medias


################################################################################

#Mean comparision (2 groups)

#1. Describe the two variables involved in the hypothesis
# en este caso vamos a ver si el hecho de que sean working days (qualitativa) es significante
# para el numero de bicicleta alquiladas (quantitativa)

# Rentals

wbr.cnt.describe()
plt.hist(wbr.cnt)
x= wbr.cnt
plt.hist(x, bins=10,edgecolor='black')

################

# Working Days
# Modo 1, creamos una variable nueva reemplazando directamente
wbr.loc[(wbr['workingday']==0), "wd"]="No" #Creamos la variable wd para que nos diga si es workingday o no
wbr.loc[(wbr['workingday']==1), "wd"]="Yes"
mytable = pd.crosstab ( wbr ["wd"],columns="count")
# Modo 2, creamos una variable nueva y la reemplazamos sustituyendo los valores
wbr["wd_st"] = wbr.workingday
wbr.wd_st = wbr.wd_st.replace(to_replace=0, value="No")
wbr.wd_st = wbr.wd_st.replace(to_replace=1, value="Yes")
# Modo 3, creamos una nueva variable por categorías
my_categories=["No","Yes"]
my_datatype= CategoricalDtype(categories=my_categories, ordered= True)
wbr["wd"] = wbr.wd.astype(my_datatype)


# Creamos la tabla
mytable = pd.crosstab ( wbr ["wd"],columns="count") # Aquí le estamos diciendo lo que irá en los ejes "x" y "y"

# Hacemos el porcentage
n= mytable.sum()
mytable2 = (mytable /n)*100 # Aquí hacemos la tabla de porcentages sobre la tabla con valores absolutos

#Modificamos la tabla
plt.bar(mytable2.index, mytable2['count']) 
plt.xlabel('Working day')
plt.title('Figure5. Percentage of Working days')
plt.show()

##################
                    
#2. Perform the numeric test: t.test


#Descriptive comparison: 
wbr.groupby('wd').cnt.mean()

# Statistical Comparison
#Extract the two sub samples and store them in two objects
cnt_wd = wbr.loc[wbr.wd=="Yes", "cnt"] #Aquí lo que estamos haciendo es crear un objeto "cnt_wd" que nos devolverá
# el número (cnt) de todas las líneas en las que el wd sea "Yes" '''
cnt_nwd = wbr.loc[wbr.wd== "No", "cnt"] #'''Aquí lo que estamos haciendo es crear un objeto "cnt_nwd" que nos devolverá
#el número (cnt) de todas las líneas en las que el wd sea "No" '''

#Perform a t test for mean comparison
import scipy.stats as stats

comp = stats.ttest_ind(cnt_wd, cnt_nwd, equal_var = False) # Esto nos devuelve un statistic y un pvalue
print(comp) # Es un numerical test
#Como el pvalue no es menor que 0.05, el working day no es determinante. Para que sea determinante, el pvalue tendría que ser inferior a 0'5

##################

# 3. Perform the graphic test: plot of the means
# 4. When posible: combine both numeric and graphic in same plot

#CI meanplot
import seaborn as sns
import matplotlib.pyplot as plt
plt.figure(figsize=(5,5))
ax = sns.pointplot(x="wd", y="cnt",
data=wbr,ci=95, join=0)
plt.yticks(np.arange(3000, 7000, step=500))
plt.ylim(2800,6200)
plt.axhline(y=wbr.cnt.mean(),
linewidth=1,
linestyle= 'dashed',
color="green")
props = dict(boxstyle='round' , facecolor='white', lw=0.5)
plt.text(0.85,5400,'Mean:4504.3''\n''n:731' '\n' 't:1.601' '\n' 'Pval.:0.110', bbox=props)
plt.xlabel('Working Day')
plt.title('Figure 6. Average rentals by Working Day.''\n')
# Concluimos que el hecho de que sea working day, no implica que se alquilen más o menos bicicletas




#Hacemos los mismo comparando los años 11 y 12
#Mean comparision (2 groups)


#1. Describe the two variables involved in the hypothesis
# en este caso vamos a ver si el hecho de que sean working days (qualitativa) es significante
# para el numero de bicicleta alquiladas (quantitativa)

# Rentals

wbr.cnt.describe()
plt.hist(wbr.cnt)
x= wbr.cnt
plt.hist(x, bins=10,edgecolor='black')

# Year

wbr.loc[(wbr['yr']==0), "year"]="2011" #Creamos la variable yr para que nos diga si es 2011 o 2012
wbr.loc[(wbr['yr']==1), "year"]="2012"
mytable = pd.crosstab ( wbr ["year"],columns="count")
print(mytable)


# Hacemos el porcentage
n= mytable.sum()
mytable2 = (mytable /n)*100 # Aquí hacemos la tabla de porcentages sobre la tabla con valores absolutos

#Modificamos la tabla
plt.bar(mytable2.index, mytable2['count']) 
plt.xlabel('Working day')
plt.title('Figure5. Percentage of Working days')
plt.show()
                    
#2. Perform the numeric test: t.test


#Descriptive comparison: 
wbr.groupby('year').cnt.mean()

# Statistical Comparison
#Extract the two sub samples and store them in two objects
cnt_2011 = wbr.loc[wbr.year=="2011", "cnt"] #Aquí lo que estamos haciendo es crear un objeto "cnt_2011" que nos devolverá
# el número (cnt) de todas las líneas en las que el wd sea "2011" '''
cnt_2012 = wbr.loc[wbr.year== '2012', "cnt"] #'''Aquí lo que estamos haciendo es crear un objeto "cnt_2012" que nos devolverá
#el número (cnt) de todas las líneas en las que el wd sea "2012" '''

#Perform a t test for mean comparison
import scipy.stats as stats

comp = stats.ttest_ind(cnt_2011, cnt_2012, equal_var = False) # Esto nos devuelve un statistic y un pvalue
print(comp) # Es un numerical test
#Como el pvalue no es menor que 0.05, el working day no es determinante. Para que sea determinante, el pvalue tendría que ser inferior a 0'5

# 3. Perform the graphic test: plot of the means
# 4. When posible: combine both numeric and graphic in same plot

#CI meanplot
import seaborn as sns
import matplotlib.pyplot as plt
plt.figure(figsize=(5,5))
ax = sns.pointplot(x="year", y="cnt",
data=wbr,ci=95, join=0)
plt.yticks(np.arange(3000, 7000, step=500))
plt.ylim(2800,6200)
plt.axhline(y=wbr.cnt.mean(),
linewidth=1,
linestyle= 'dashed',
color="green")
props = dict(boxstyle='round' , facecolor='white', lw=0.5)
plt.text(0.85,4400,'Mean:4504.3''\n''n:731' '\n' 't:18.6' '\n' 'Pval.:0.000', bbox=props)
plt.xlabel('Year')
plt.title('Figure 7. Average rentals by year.''\n')

###############################################################################

#Mean comparison( > 2 groups)
# Vamos a analizar si el tiempo que hace es determinante a la hora de alquilar bicicletas


#1. Describe the two variables involved in the hypothesis

#Rentals (Quantitativa)

wbr.cnt.describe
plt.hist(wbr.cnt)


#Weathercondition (Qualitativa)

mytable = wbr.groupby(['weathersit']).size()
n = mytable.sum()
mytable2 = (mytable/n)*100
print(mytable2)
barlist = ['Sunny', 'Cloudy', 'Rainy'] # Le damos nombre a los atributos de la variable que son 1, 2 y 3
plt.bar(barlist, mytable2)
plt.ylabel('Percentage')
plt.xlabel("weather")



# 2. Perform the numeric test:


##Descriptive comparison
wbr.groupby('weathersit').cnt.mean()

#Statistical comparison
cnt_sunny=wbr.loc[wbr.weathersit==1, "cnt"] # relacionamos el cnt_sunny con todas las cnt donde el weathersit sea 1
cnt_cloudy=wbr.loc[wbr.weathersit==2, "cnt"]
cnt_rainy=wbr.loc[wbr.weathersit==3, "cnt"]

res = stats.f_oneway(cnt_sunny, cnt_cloudy, cnt_rainy)

print(res)

print(round(res[0],3), round(res[1],3))
# Esto nos da un pvalue menos que 0.05, por tanto, esta variable si que es vinculante


# 3. Perform the graphic test: plot of the means

# 4. When posible: combine both numeric and graphic in same plot

#Graphic comparison: confidence intervals for the means

plt.figure(figsize=(5,5))
ax= sns.pointplot(x="weathersit", y="cnt", data=wbr, capsize=0.05, ci=99.9, join=0)
ax.set_ylabel('')
plt.yticks(np.arange(1000, 7000, step=500))
plt.ylim(800,6200)
plt.axhline(y=wbr.cnt.mean(), 
linewidth=1, 
linestyle= 'dashed', color="green")
props = dict(boxstyle='round', facecolor='white', lw=0.5)
plt.text(1.5, 5000, 'Mean: 4504.3''\n''n: 731' '\n' 'F: 40.06' '\n' 'Pval.: 0.000',    bbox=props)
plt.xlabel('Weather Situation')
plt.title('Figure 8. Average rentals by Weather Situation.''\n')

ax = sns.boxplot(x="weathersit", y="cnt", data=wbr) #How to create a boxplot



