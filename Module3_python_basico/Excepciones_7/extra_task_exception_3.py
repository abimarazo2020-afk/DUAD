'''Create a function `sum_values(list)` that:
Receives a list of elements (strings, integers, mixed floats)
Attempts to convert each element to type `float`
If successful, sums the value and displays: "<value> summed successfully"
If unsuccessful, displays: "Invalid element: <value>"
Finally, prints the total sum'''

def sum_values(list_sum):

    total_floats = 0
    for value in list_sum:

        try:
            total_floats += float(value)
            print(f'{value} summed successfully')

        except ValueError as error:
            print(f'Invalid element: {value}, {error}')

    
    return total_floats

result = sum_values(['5', 'hello', 9, 'here', 8, 8.2])
print(result)

