
'''EJERCICIO#2
Create a program that opens a .csv file containing video game information (based on the CSV file generated in exercise 1) and:
Reads the video game CSV file
Asks the user for an ESRB rating (for example: "T")
Displays all video games with that rating'''

import csv

def open_and_read_csv(file_path):
    user_esrb = input('Enter your esrb: ')
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if user_esrb == row['ESRB Rating']:
                print(row)
                           
            

open_and_read_csv('games.csv')
