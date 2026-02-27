
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

