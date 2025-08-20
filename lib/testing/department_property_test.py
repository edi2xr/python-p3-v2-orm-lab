import pytest
from lib.department import Department

def test_department_name_property():
    dept = Department("HR")
    assert dept.name == "HR"
