
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
