def get_number_to_operate():
    try:
        new_number = int(input('Ingrese el numero a operar :'))
        return new_number
    except ValueError as error:
        print(f'the element is not a valid number, Error: {error}')
        return None

def addition(current_number):
    new_number = get_number_to_operate()
    if new_number is None:
        return current_number
    result_sum = (new_number + current_number)
    print(f'the result of {current_number} + {new_number} is {result_sum}')
    current_number = result_sum
    print(f'new current number: {current_number}')

    return current_number
    
def rest(current_number):
    new_number = get_number_to_operate()
    if new_number is None:
        return current_number
    result_rest = (current_number - new_number)
    print(f'the result of {current_number} - {new_number} is {result_rest}')
    current_number = result_rest
    print(f'new current number: {current_number}')

    return current_number



def multiplication(current_number):
    new_number = get_number_to_operate()
    if new_number is None:
        return current_number
    result_multiplication = (new_number * current_number)
    print(f'the result of {new_number} * {current_number} is {result_multiplication}')
    current_number = result_multiplication
    print(f'new current number: {current_number}')

    return current_number


def division(current_number):
    new_number = get_number_to_operate()
    if new_number is None:
        return current_number

    try:
        result_division = current_number / new_number
    except ZeroDivisionError:
        print("Cannot divide by zero")
        return current_number

    print(f'the result of {current_number} / {new_number} is {result_division}')
    current_number = result_division
    print(f'new current number: {current_number}')

    return current_number



def main():
    current_number = 0

    while True:
        print("\nCurrent number:", current_number)
        print("0. Addition")
        print("1. Subtraction")
        print("2. Multiplication")
        print("3. Division")
        print("4. Exit")

        try:
            option = int(input("Choose an option: "))
        except ValueError:
            print("Invalid option")
            continue

        if option == 0:
            current_number = addition(current_number)
        elif option == 1:
            current_number = rest(current_number)
        elif option == 2:
            current_number = multiplication(current_number)
        elif option == 3:
            current_number = division(current_number)
        elif option == 4:
            print("Goodbye")
            break
        else:
            print("Invalid option")


main()
