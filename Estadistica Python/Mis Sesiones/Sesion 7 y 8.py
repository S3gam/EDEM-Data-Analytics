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
wbr.shape
wbr.head()

###################################################
# Percentage Comparisons, relacionamos una variable QUALITATIVA con otra QUALITATIVA

# Dependent Variable es la Variable dependiente sobre la que vamos a analizar los posibles cambios, en este caso las rentals
#Recoding DV for analysis, we Recode de DV in order to make it a nominal variable
res = wbr.cnt.describe()
print (res)
# Store parameters as numbers
m  = res[1]
sd = res[2]
n  = res[0]

### Recode cnt to string
wbr.loc[  (wbr['cnt']<(m-sd)) ,"cnt_str"]= "Low rentals"
wbr.loc[ ((wbr['cnt']>(m-sd)) & (wbr['cnt']<(m+sd))) ,"cnt_str"]= "Average rentals"
wbr.loc[  (wbr['cnt']>(m+sd)) ,"cnt_str"]= "High rentals"


### Recode cnt to ordinal
my_categories=["Low rentals", "Average rentals", "High rentals"]
my_rentals_type = CategoricalDtype(categories=my_categories, ordered=True)
wbr["cnt_cat"] = wbr.cnt_str.astype(my_rentals_type)
wbr.info()

### frequencies & barchart

mytable = pd.crosstab(wbr.cnt_cat, columns="count", normalize='columns')*100
print(mytable)
print (round(mytable,1))
plt.bar(mytable.index, mytable['count'])
plt.show()


# Recode  weather situation
# To string
#Weathercondition

mytable = wbr.groupby(['weathersit']).size()
n = mytable.sum()
mytable2 = (mytable/n)*100
print(mytable2)
barlist = ['Sunny', 'Cloudy', 'Rainy']
plt.bar(barlist, mytable2)
plt.ylabel('Percentage')

wbr.loc[(wbr['weathersit']==1), "season_cat"]="Sunny"
wbr.loc[(wbr['weathersit']==2), "season_cat"]="Cloudy"
wbr.loc[(wbr['weathersit']==3), "season_cat"]="Rainy"


my_categories =["Sunny", "Cloudy", "Rainy"]


#Step 2: Define new data type
my_seasons_type = CategoricalDtype ( categories= my_categories , ordered=True)

# Second create a new categorical_ordered variable using our specific data type
wbr["estacion"] = wbr.season_cat.astype(my_seasons_type) # Hemos creado una variable nueva en el wbr llamada estación

mytable= pd.crosstab(index=wbr["estacion"], columns="count")
print(mytable)
n=mytable.sum()

mytable2=(mytable/n)*100
print(mytable2)


#Crosstabulation


my_ct= pd.crosstab(wbr.cnt_cat,wbr.season_cat,normalize='columns', margins= True)*100

my_ct= round(my_ct,1)

#Statistical test
ct = pd.crosstab(wbr.cnt_cat, wbr.season_cat)

#Tabla de contingencia: hay que quitar la ultima columna (sin el total)
ct
stats.chi2_contingency(ct)

#Plotting the cross tabulation

#Transpose and plot
my_ct2 = my_ct.transpose()
#my_ct2.plot(kind= "bar", edgecolor= "black")
my_ct2.plot(kind= "bar", edgecolor= "black", colormap="Blues") #Transposed
props= dict(boxstyle='round', facecolor='white', lw=0.5)
plt.legend(['Low rentals', 'Average rentals', 'High rentals'])
plt.text(-0.4,81, 'Chi2: 68.765' '\n' 'n: 731' '\n' 'Pval:0.000',    bbox=props)
plt.xlabel('Weather situation')
plt.title('Figure 7. Percentage of rental level, by weather situation. '' \n')
plt.xticks(rotation='horizontal')
plt.ylim(0,100)







