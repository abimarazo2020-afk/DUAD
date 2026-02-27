'''EJERCICIO#4
Create a program that opens a .csv file containing video game information
 (based on the CSV file generated in exercise 1) and:
Reads the .csv file containing video games
Asks the user to enter the name of a developer (e.g., "Ubisoft")
Displays all video games developed by that company in a readable format:'''

import csv

def open_and_read_csv(file_path):
    developer_name = input('Enter your developer name: ')
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)

        for row in reader:
            if developer_name == row['Developer']:
                print('Game:', row['Name'])
                print('Developer:', row['Developer'])

open_and_read_csv('games.csv')