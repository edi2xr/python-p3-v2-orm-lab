from lib.debug import Base
from lib.department import Department
from lib.db import CONN, CURSOR

class Employee(Base):
    def __init__(self, name, department: Department):
        self.name = name
        self.department = department
