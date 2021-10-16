'''
TIPOS DE DATOS EN PYTHON
'''

# STR
micadena: str = "hola mundo"
micadena2: str = '''Hola mundo'''

primeros_dos_caracteres= micadena[0:2]
print(f'PRIMEROS DOS CARACTERES: {primeros_dos_caracteres}')
print(F'texto con mayusculas: {micadena.upper()}')
print(F'texto con minusculas: {micadena.lower()}')
'''
LISTAS de datos
'''
milista: [str] = {"martin", "Juan", "Ana"}
print(milista)
print(*milista)
print(*milista
)
# RANGOS
mirango = range(1, 10, 2)
mirango2 = range(1, 100, 10)
print(*mirango2)
'''
Diccionarios
'''
persona = {"nombre": "Sergi", "edad": "24", "email": "segam@gmail.com"}
print(persona)
print(*persona)
print(f'La edad de {persona["nombre"]} es {persona.get("edad")}')

misnumeros = [1,2,3,4,5,1,5]
print(*misnumeros)
miSetDeNumeros = set([1,2,3,4,5,1,5])
print(*miSetDeNumeros)
miSetDeNumeros2 = set(misnumeros)
print(miSetDeNumeros2)

miValorNone = None

print(miValorNone)


'''
str
int
float
complex
list
tuple
range
dict
set
frozenset
bool
bytes
bytearray
memoryview
'''

resultado_operacion:float = ((6-2)/(5))**2
print(resultado_operacion)
print(resultado_operacion.__round__(4))


'''
RETO GRUPAL

Partiendo de:
- cantidad a invertir - 5000
- el interés anual - 0.2
- El número de años - 6

Calcular el capital

'''

inv = 5000
N = 6

CapitalFinal:float = (inv * (1+(inv/100))**N)
print(CapitalFinal.__round__(2))




''' 
· Los artículos de temporada tendrán un 30% de descuento
· Recibe numero de productos de temporada
· Recibe numero de productos de la temporada pasada
· Aplicar descuento para obtener el gasto total de productos
· Decir al usuario lo que se ahorra
'''

venta = 14.99
Descuento = 0.3

temporada = int(input("Numero de productos que son de temporada"))
NoTemporada = int(input("Numero de productos que no son de temporada"))
Total = (temporada*venta) + (NoTemporada*(venta*(1-Descuento)))


while True:
  year = int(input('introducir el año'))
  if (year % 4) == 0 & (year % 400) == 0:
    if (year % 100) !=0:
      print(f' El año (year) es bisiesto')
  else:
    print(f'el año (year) no es bisiesto')
    