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





