"""EJERCICIO#2
Create pseudocode that asks the user for a time in seconds and calculates whether it is less than or greater than 10 minutes.
If it is less, display how many seconds are needed to reach 10 minutes. If it is greater, display "Greater than".
If it is exactly equal, display "Equal".
"""

time_in_seconds = int(input('Enter your time in seconds:'))
missing_seconds = 0

if(time_in_seconds < 600):
    missing_seconds = (600 - time_in_seconds)
    print(f'The seconds that would be missing are{missing_seconds}')

elif(time_in_seconds > 600):
    print('Major')

else:
    print('Same')