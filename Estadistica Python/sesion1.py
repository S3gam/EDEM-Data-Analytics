import os                              #sistema operativo
import pandas as pd                    #gestionar dataframes
import numpy as np                     #numeric python vectores
import matplotlib.pyplot as plt        #graficos

name = ['Yaling', 'Sofia', 'Maria', 'Pablo', 'Ines']
age = [28, 23, 25, 23, 25]
gender =['Female', 'Female', 'Female', 'Male', 'Female' ]

print(name, age, gender)

class2020 = pd.DataFrame({'name': name, 'age' : age, 'gender': gender})

del (age,gender,name)

class2020.shape                       #Nos da el numero de filas y las columnas
class2020.head(3)                     #
class2020.tail(2)
#QC OK 12/11/2021

edad  = class2020.age                 #Recuperar age con el nombre de edad
del(edad)


#Get working directory
os.getcwd()

#Change working directory

#Decir donde quiere poner el directorio de trabajo
os.chdir(r'C:\Users\Chemagdlc\Desktop\Chema\EDEM\estadisticaPython\01_Sesiones\sesion1')
os.getcwd()

# Save dataframe to Exel or csv
class2020.to_excel("class2020.xlsx")
class2020.to_csv("class2020.csv")



