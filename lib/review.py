from lib.debug import Base
from lib.employee import Employee
from lib.db import CONN, CURSOR

class Review(Base):
    def __init__(self, employee: Employee, comment):
        self.employee = employee
        self.comment = comment
