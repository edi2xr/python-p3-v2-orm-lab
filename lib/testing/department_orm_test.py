import pytest
from lib.db import CONN, CURSOR
from lib.department import Department

def test_department_creation():
    dept = Department("Engineering")
    assert dept.name == "Engineering"
