'''JSON en PYTHON'''

#Python tiene un paquete integrado llamado json, que se puede utilizar para trabajar con datos JSON.

import json



'''Analizar JSON: convertir de JSON a Python'''

#El resultado será un diccionario de Python .





'''Convertir de JSON a python'''

import json #Sin esto, Python no sabría qué es json.loads().

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}' #JSON usa comillas dobles " " obligatoriamente.

# parse x:
y = json.loads(x) #json.loads() significa load string (cargar desde un string)

# the result is a Python dictionary:
print(y["age"]) #Accedes al valor asociado a la clave "age" del diccionario y.


#R/ 30


# x es una cadena de texto (string).
# El contenido de esa cadena está en formato JSON.
# Aunque se parece a un diccionario, todavía no lo es: sigue siendo solo texto.
#y = json.loads(x) Convierte el texto JSON en un diccionario de Python.
#Ahora Python puede trabajar con esos datos directamente.




'''   Convertir de Python a JSON   '''

import json

# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)  #json.dumps() significa dump string (volcar a string).

# the result is a JSON string:
print(y)


#R/ {"name": "John", "age": 30, "city": "New York"}

# x es un diccionario de Python.
# Usa claves y valores normales de Python.
# Esto NO es JSON, es un objeto de Python.
# Diferencia clave:
# Python permite comillas simples o dobles
# JSON exige solo comillas dobles
# json.dumps() significa dump string (volcar a string).
# Convierte el diccionario de Python en un string en formato JSON.
# x es un diccionario de Python
# json.dumps(x) crea una versión nueva de x, pero:
# convertida a texto (string)
# en formato JSON
# Ese texto se guarda en y
# 📌 En otras palabras:
# x 👉 dict (objeto Python)
# y 👉 string (JSON)





'''EJEMPLOS DE DATOS QUE SE PUEDEN CONVERTIR A JSON'''

import json

print(json.dumps({"name": "John", "age": 30})) #dic
print(json.dumps(["apple", "bananas"])) #list
print(json.dumps(("apple", "bananas"))) #tuple
print(json.dumps("hello")) #string
print(json.dumps(42)) #int
print(json.dumps(31.76)) #float
print(json.dumps(True)) #bool
print(json.dumps(False)) #bool
print(json.dumps(None)) #none




'''Al convertir de Python a JSON, 
los objetos de Python se convierten en el equivalente JSON (JavaScript):'''


# Python    	JSON
# dict      	Object
# list	        Array
# tuple	        Array
# str	        String
# int	        Number
# float	        Number
# True	        true
# False	        false
# None	        null



'''Convierte un objeto Python que contenga todos los tipos de datos legales y muestralo:'''

import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}


print(json.dumps(x))


#R/
#{"name": "John", "age": 30, "married": true, "divorced": false, "children": ["Ann", "Billy"], 
# "pets": null, "cars": [{"model": "BMW 230", "mpg": 27.5}, {"model": "Ford Edge", "mpg": 24.1}]}





'''Formatear el resultado
El ejemplo anterior imprime una cadena JSON, 
pero no es muy fácil de leer, sin sangrías ni saltos de línea.'''


#El json.dumps()método tiene parámetros para facilitar la lectura del resultado:


'''Utilice el indentparámetro para definir el número de sangrías:'''

json.dumps(x, indent=4)


'''También puede definir los separadores, el valor predeterminado es (", ", ": "), 
lo que significa utilizar una coma y un espacio para separar cada objeto, y dos puntos 
y un espacio para separar las claves de los valore'''


'''Utilice el separatorsparámetro para cambiar el separador predeterminado:'''

json.dumps(x, indent=4, separators=(". ", " = "))





'''El json.dumps()método tiene parámetros para ordenar las claves en el resultado:'''

'''Utilice el sort_keysparámetro para especificar si el resultado debe ordenarse o no:'''


json.dumps(x, indent=4, sort_keys=True)