
'''EJERCICIO#3
Create a program that opens a .csv file containing video game information 
(based on the CSV file generated in exercise 1) and:
Reads the .csv file containing video games
Counts how many video games there are in each genre
Displays the results in an organized manner'''

import csv

def open_and_read_csv(file_path):
    action_counter = 0
    adventure_counter = 0
    sandbox_counter = 0

    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)

        for row in reader:
            if row['Genre'] == "Action":
                action_counter += 1
            elif row['Genre'] == "Adventure":
                adventure_counter += 1
            elif row['Genre'] == "Sandbox":
                  sandbox_counter += 1

    print("Cantidad de videojuegos por género:")
    print("Action:", action_counter)
    print("Adventure:", adventure_counter)
    print("Sandbox:", sandbox_counter)

open_and_read_csv("games.csv")