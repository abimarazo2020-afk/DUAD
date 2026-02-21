''' este es un archivo CSV con información de ventas de una tienda:'''

#Fecha,Total de ventas,Total de descuentos,Total de ingresos,Total de ganancia neta
# 02/02/2022,4532.43,234.23,4298.2,3123.2
# 03/02/2022,3731.63,253.43,3497.4,2323.4
# 04/02/2022,5123.34,345.87,4777.47,3895.32

# La primera línea son los nombres de cada columna.
# Las filas posteriores son los valores de cada día, separando los de cada columna con una coma.




'''                                 LECTURA                                '''



''''Vamos a leer el siguiente archivo que tenmos aqui arriba y vamos a imprimir sus lineas'''

import csv #modulo 


def read_csv_file(file_path):
  with open(file_path, 'r') as file:
    reader = csv.DictReader(file) #objecto
    for row in reader:
      print(row)

read_csv_file('ventas.csv')


#R/ en diccionario: 

#{'Fecha': '02/02/2022', 'Total de ventas': '4532.43', 'Total de descuentos': '234.23', 'Total de ingresos': '4298.2', 'Total de ganancia neta': '3123.2'}
#{'Fecha': '03/02/2022', 'Total de ventas': '3731.63', 'Total de descuentos': '253.43', 'Total de ingresos': '3497.4', 'Total de ganancia neta': '2323.4'}
#{'Fecha': '04/02/2022', 'Total de ventas': '5123.34', 'Total de descuentos': '345.87', 'Total de ingresos': '4777.47', 'Total de ganancia neta': '3895.32'}



 
'''                                ESCRITURA                           '''




'''creemos un nuevo archivo usando datos de países:'''


import csv


countries_list = [
	{
		'name': 'Costa Rica',
		'capital': 'San José',
		'currency': 'Colón',
		'area_km2': '51,100',
	},
	{
		'name': 'Colombia',
		'capital': 'Bogotá',
		'currency': 'Peso Colombiano',
		'area_km2': '1,141,748',
	},
	{
		'name': 'México',
		'capital': 'Ciudad de México',
		'currency': 'Peso Mexicano',
		'area_km2': '1,972,550',
	},
]

country_headers = (
	'name',
	'capital',
	'currency',
	'area_km2',
)

def write_csv_file(file_path, data, headers):
  with open(file_path, 'w', encoding='utf-8') as file:
    writer = csv.DictWriter(file, headers) #crea un objecto que permite escribir CSV usando dics
    writer.writeheader() #escribe la primera linea de codigo
    writer.writerows(data) #escribe todas las lineas de data
 
write_csv_file('countries.csv', countries_list, country_headers)


#R/

# name,capital,currency,area_km2

# Costa Rica,San José,Colón,"51,100"

# Colombia,Bogotá,Peso Colombiano,"1,141,748"

# México,Ciudad de México,Peso Mexicano,"1,972,550"

