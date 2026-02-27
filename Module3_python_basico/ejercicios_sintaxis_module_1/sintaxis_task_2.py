""" EJERCICIO#2
Create a program that asks the user for their first name, last name, and age.
Display whether they are a baby, child, preteen, teenager, young adult, adult, or senior citizen.
"""

name = input('Enter your name:')
last_name = input('Enter your last name:')
age = int(input('Enter your age:'))

if(age <= 6):
    print('You are a baby')

elif(age <= 12):
    print('You are a child')

elif(age <= 18):
    print('You are a teenager')

elif(age <= 35):
    print('you are a young adult')

elif(age < 65):
    print('you are an adult')

else:
    print('you are an older adult')

print(f'Your name is {name} {last_name} and your age is: {age}')