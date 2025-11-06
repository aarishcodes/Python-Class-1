# employee = []

# def add_employee(employee):
#     employee.append(employee)
#     print("Employ added successfully")

# def update_employee(id, salary):
#     index = search_employee(id)

#     if index != -1:
#         employee = employee[index]
#         new_employee = (employee[0], employee[1], salary)
#         employee[index] = new_employee
#         print("employee updated successfully")


class Student:
    
    def __init__(self, name):
        self.name = name
        print("Constructor called")

s1 = Student("Aarish")
print(s1.name)

s2 = Student("faiz")
print(s2.name)

