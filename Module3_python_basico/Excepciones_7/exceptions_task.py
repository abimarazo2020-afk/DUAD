'''Create a command-line calculator. 
It should display a current number and a menu to select the operation to perform on another number:
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Clear Result
When an option is selected, the user should enter the new number to be added, reset, multiplied, or divided by the current number. The result should then become the new current number.
The calculator should display error messages if the user selects an invalid option or enters an invalid number during the operation.'''


current_number = 18
print('Esta es su calculadora')
print(f'Lista de opciones que puede realizar usando {current_number}')
print('1. addition')
print('2. rest')
print('3. multiplication')
print('4. division')
print('5 clear result')

while True:
    option = int(input('Ingrese su opcion del 1 al 5'))
    
    if option == 1:
        try:
            new_number = int(input('Ingrese el numero a operar :'))
        except ValueError as error:
            print(f'El elemento de la lista no es un numero valido. Error: {error}')
            continue

        result_sum = (new_number + current_number)
        print(f'the result of {current_number} + {new_number} is {result_sum}')
        current_number = result_sum
        print(f'new current number: {current_number}')

    elif option == 2:
        try:
            new_number = int(input('Ingrese el numero a operar :'))
        except ValueError as error:
            print(f'El elemento de la lista no es un numero valido. Error: {error}')

            continue

        result_rest = (current_number - new_number)
        print(f'the result of {current_number} - {new_number} is {result_rest}')
        current_number = result_rest
        print(f'new current number: {current_number}')

    elif option == 3:
        try:
            new_number = int(input('Ingrese el numero a operar :'))
        except ValueError as error:
            print(f'El elemento de la lista no es un numero valido. Error: {error}')
        
            continue

        result_multiplication = (new_number * current_number)
        print(f'the result of {new_number} * {current_number} is {result_multiplication}')
        current_number = result_multiplication
        print(f'new current number: {current_number}')

    elif option == 4:
        try:
            new_number = int(input('Ingrese el numero a operar :'))
        except ValueError as error:
            print(f'El elemento de la lista no es un numero valido. Error: {error}')
            continue

        try:
            result_division = (current_number / new_number)

        except ZeroDivisionError as es:
            print(f'El elemento no se puede divir por 0. Error: {es}')

            continue

        print(f'the result of {current_number} / {new_number} is {result_division}')
        current_number = result_division
        print(f'new current number: {current_number}')
 
    elif option == 5:
       current_number = 0
       print('the result has been cleaned')

    else:
       print('invalid option')