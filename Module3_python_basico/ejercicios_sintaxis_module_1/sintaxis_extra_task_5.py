"""EJERCICIO#5
Create a flowchart that asks the user for 3 numbers. 
If one of those numbers is 30, or if the sum of the 3 numbers is 30, display “Correct”. 
Otherwise, display “Incorrect”.
"""

number1 = int(input('Enter the number1:'))
number2 = int(input('Enter the number2:'))
number3 = int(input('Enter the number3:'))
addition = number1 + number2 + number3

if(number1 == 30):
    print('Correct')

elif(number2 == 30):
    print('Correct')

elif(number3 == 30):
    print('correct')

elif(addition == 30):
    print('correct')

else:
    print("incorrect")