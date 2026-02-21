'''EJERCICIO#1
Create a program that opens a .json file containing Pokémon information (based on the JSON generated
in exercise 1) and reads the Pokémon JSON file.
Iterates through the list of Pokémon and displays their name, type, and level 
(or any other defined attributes) in the console.
'''

import json

def read_and_open_file(path):
    with open(path, 'r', encoding='utf=8') as file:
        return json.load(file)
    

def main():

    pokemons = read_and_open_file("pokemons.json") 

    for pokemon in pokemons:
        print('Name:', pokemon["name"])
        print('level:', pokemon["level"])
        print('type:', pokemon["type"])
        

if __name__ == "__main__":
    main()






'''EJERCICIO#2
Create a program that opens a .json file containing Pokémon information (based on the JSON generated in exercise 1) and:
Reads the Pokémon JSON file
Asks the user for a Pokémon type
Displays all Pokémon of that type'''

import json

def read_and_open_file(path):
    with open(path, 'r', encoding='utf-8') as file:
        return json.load(file)

def main():
    pokemons = read_and_open_file("pokemons.json")
    input_pokemon_name = input('Enter the pokemon type you are looking for (Water,Electric,FFire):')

    for pokemon in pokemons:
        if input_pokemon_name in pokemon["type"]: #esto se hace asi porque type es una lista 
            #if pokemon["type"] == input_pokemon_name esta hubiera funcionado si type fuera string nada mas 
            print(pokemon["name"])


if __name__ == "__main__":
    main()






'''EJERICIC#3
 Create a program that opens a .json file containing Pokémon information (based on the JSON generated in exercise 1) and:
Read the Pokémon JSON file.
For each Pokémon, display its main stats (e.g., attack, defense, speed, etc.).
Example:'''

import json

def read_and_open_file(path):
    with open(path, 'r', encoding='utf-8') as file:
        return json.load(file)

def main():
    pokemons = read_and_open_file("pokemons.json")

    for pokemon in pokemons:
        print('Name:', pokemon["name"])
        print('Attack:', pokemon["base"]["Attack"])
        print('Defense:', pokemon["base"]["Defense"])
        print('Speed:', pokemon["base"]["Speed"])

if __name__ == "__main__":
    main()




'''EJERCICIO#4
Create a program that opens a .json file containing Pokémon information (based on the JSON generated in exercise 1) and:
Read the JSON file
Group the Pokémon by type (e.g., "water", "fire", etc.)
Calculate and sample the average level for each type:'''

import json

# Función para abrir y leer el archivo JSON
def open_and_read_file(path):
    with open(path, 'r', encoding='utf-8') as file:
        return json.load(file)  # Convierte el JSON en una lista de diccionarios de Python

# Función principal
def main():
    # Abrimos el archivo y guardamos la lista de Pokémon
    pokemons = open_and_read_file("pokemons.json")
    
    # Diccionario donde guardaremos los datos por tipo
    type_dict = {}

    # Recorremos cada Pokémon en la lista
    for pokemon in pokemons:
        level = pokemon["level"]  # Guardamos el nivel del Pokémon

        # Recorremos cada tipo del Pokémon (puede tener varios)
        for type in pokemon["type"]:
            # Si es la primera vez que vemos este tipo, lo inicializamos en el diccionario
            if type not in type_dict:
                type_dict[type] = {"sum": 0, "count": 0}

            # Sumamos el nivel a la suma acumulada para este tipo
            type_dict[type]["sum"] += level

            # Contamos un Pokémon más para este tipo
            type_dict[type]["count"] += 1

    # Calculamos y mostramos el promedio de nivel por tipo
    for type, data in type_dict.items():
        average = data["sum"] / data["count"]  # promedio = suma de niveles / cantidad de Pokémon
        print(f"{type}: Average level = {average}")

# Ejecutamos la función principal
if __name__ == "__main__":
    main()

# tipo → se asigna a la clave del diccionario
# Ejemplo: "water" o "Fire"

# data → se asigna al valor correspondiente, que en este caso es otro diccionario con los contadores
# Ejemplo: {"suma": 12, "cantidad": 2}            

# data["suma"] → toma la suma acumulada de niveles para ese tipo

# data["cantidad"] → toma cuántos Pokémon tiene ese tipo

# promedio → calcula la media de niveles

# tipo → solo sirve para imprimir qué tipo estamos mostrando
        
