import pytest
from lib.db import CONN, CURSOR
from lib.employee import Employee
from lib.department import Department

def test_employee_creation():
    dept = Department("Finance")
    emp = Employee("Alice", dept)
    assert emp.name == "Alice"
    assert emp.department == dept
