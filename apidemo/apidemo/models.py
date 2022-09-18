from datetime import date

from django.db import models
from ninja import Schema


class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birthdate = models.DateField(null=True, blank=True)


class EmployeeIn(Schema):
    first_name: str
    last_name: str
    birthdate: date = None


# Writing it is not required but there are benefits in writing it
# - validation
# - documentation
# - ORM to JSON conversions
class EmployeeOut(Schema):
    id: int
    first_name: str
    last_name: str
    birthdate: date = None
