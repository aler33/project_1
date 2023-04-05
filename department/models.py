from django.db import models
from employees.models import Employee


class Department(models.Model):
    name = models.CharField(max_length=64, blank=True)
    director = models.OneToOneField(Employee, on_delete=models.DO_NOTHING, blank=True, null=True)
