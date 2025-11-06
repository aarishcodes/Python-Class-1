import pickle
import os


FILE_NAME = 'employee_db.dat'

def read_employee():
    if not os.path.exists(FILE_NAME):
        return []
    else:
        with open(FILE_NAME, 'rb') as input_file:
            return pickle.load(input_file)
        
def write_employee(employee):
    with open(FILE_NAME, 'rb') as output_file:
        pickle.dump(employee, output_file)