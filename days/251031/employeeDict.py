print("ASSIGNEMENT")
print("Employee Management System (Storage Dictonary)")

employees = {}


# creating the employee
def create_employee(employee_id, name, position):
    employees[employee_id] = {name: name, position: position}
    print(f'Employee {name} added successfully')

# updating the employee
def update_employee(employee_id, name, position):
    if employee_id in employees:
        employees[employee_id] = {'name': name, 'position': position}
        print("Employee Successfully Updated")
    else:
        print("Employee data not found")

# delete the employee
def delete_employee(employee_id):
    if employee_id in employees:
        del employees[employee_id]
        print("Successfully deleted the employee")
    else:
        print("Employee not found")


create_employee(101, 'Aarish', 'Manager')
create_employee(102, 'Salena', 'Project Manager')
create_employee(103, 'Ranbir', 'App developer')

print(employees)

update_employee(102,'Salena Gomaz', "Senior Dictory")

print(employees)

delete_employee(103)
delete_employee(102)
# delete_employee(101)

update_employee(101, "Aarish Faiz", "Senior Manager")
print(employees)