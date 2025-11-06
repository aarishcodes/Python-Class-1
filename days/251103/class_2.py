employees = []

class Employee:
    def __init__(self, id, name, job_title, salary):
        self.id = id
        self.name = name
        self.job_title = job_title
        self.salary = salary
    def __repr__(self):
        return f'Employee[id: {self.id}, name: {self.name}, job_title: {self.job_title},salary: {self.salary}]'
    
    def __str__(self):
        return self.__repr__()

employees = [Employee(101, "Aarish", "Technical Consultant Engineer", 120000),
            Employee(102, "Ranbir", "Technical Consultant Engineer", 100000)]

print(employees[0])
print(employees[1])
