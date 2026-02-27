'''EJERCICIO#2
Experiment with the concept of scope:
Try accessing a variable defined inside a function from outside.
Try accessing a global variable from within a function and changing its value.
'''

variable_two = 95


def function_three():
    global variable_two
    variable_two = 100
    variable_one = 55
    print(variable_one)
    print(variable_two)
    

function_three()
print(variable_two) # aqui el resultado es 95 porque solo se cambia dentro de la funcion

#print(variable_one)  # "variable_one" is not defined