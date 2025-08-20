import pytest
from lib.db import CONN, CURSOR
from lib.review import Review
from lib.employee import Employee
from lib.department import Department

def test_review_creation():
    dept = Department("Support")
    emp = Employee("Charlie", dept)
    review = Review(emp, "Great work!")
    assert review.employee == emp
    assert review.comment == "Great work!"
