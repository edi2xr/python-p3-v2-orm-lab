import pytest
from lib.employee import Employee
from lib.department import Department

def test_employee_department_property():
    dept = Department("Sales")
    emp = Employee("Bob", dept)
    assert emp.department.name == "Sales"
