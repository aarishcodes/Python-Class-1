import pytest
import client.repo as repo


def employee_test_create():
    employee = {
        'name': 'aarish',
        'salary': '990000'
    }


    create_employee = repo.add_employee(employee)

    quired_employee = repo.search_employee(create_employee['id'])

    #  assertion 
    assert quired_employee is not None
    assert quired_employee['name'] == employee['name']