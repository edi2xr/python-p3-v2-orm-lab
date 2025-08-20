import pytest
from lib.review import Review
from lib.employee import Employee
from lib.department import Department

def test_review_employee_property():
    dept = Department("Marketing")
    emp = Employee("Dana", dept)
    review = Review(emp, "Needs improvement")
    assert review.employee.name == "Dana"
    assert review.comment == "Needs improvement"
