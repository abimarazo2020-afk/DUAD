

"""EJERCICIO#6
Temperature unit converter
Ask the user to enter a temperature in Celsius. 
Convert it to Fahrenheit and Kelvin. Display all three values.
"""
Fahrenheit = 0
Kelvin = 0

celsius_temperature = float(input('Enter your temperature in celsius:'))
Fahrenheit = (celsius_temperature * 9/5) + 32
Kelvin = celsius_temperature + 273.15

print(f'The temperature in Celsius is: {celsius_temperature} , The temperature in Fahrenheit is {Fahrenheit} and the temperature in Kelvin is {Kelvin}')

