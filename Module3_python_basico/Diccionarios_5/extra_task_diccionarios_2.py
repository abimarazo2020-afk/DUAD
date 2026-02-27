
'''EJERCICIO#2
Group employees by department
Given a list of employees where each has a name, email, and department, create a dictionary that groups the employees by their department:
'''


employes = [
    {
        'name': 'Myron',
        'email': 'myron@cisco.com',
        'department': 'Managment'
    },

    {
        'name': 'Diego',
        'email': 'diego@cisco.com',
        'department': 'SME'
    },


    {
        'name': 'jeremy',
        'email': 'Jeremy@cisco.com',
        'department': 'SME'
    },

    {
        'name': 'Liseth',
        'email': 'liseth@cisco.com',
        'department': 'managment'
    },


    {
         'name': 'Andres',
        'email': 'Andres@cisco.com',
        'department': 'TSE'

    }


]


new_dictionary = {}


for employee in employes:
    department = employee['department']

    if department not in new_dictionary:
       new_dictionary[department] = []

    new_dictionary[department].append(employee)

print(new_dictionary)
