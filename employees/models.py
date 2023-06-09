from django.db import models
from time import time
from pathlib import Path


def employees_photo_path(instance, filename):
    num = int(time() * 1000)
    suff = Path(filename).suffix
    return 'employee_{0}/photo/{1}'.format(instance.username, f'pic_{num}{suff}')


class Employee(models.Model):
    last_name = models.CharField(max_length=64, blank=False)
    first_name = models.CharField(max_length=64, blank=False)
    sur_name = models.CharField(max_length=64, blank=True)
    photo = models.ImageField(upload_to=employees_photo_path, blank=True, null=True)
    job_title = models.CharField(max_length=64, blank=True)
    salary = models.PositiveIntegerField()
    birthday = models.DateField(blank=False)
    department_id = models.ForeignKey('department.Department', on_delete=models.DO_NOTHING, blank=True, null=True)

    @property
    def age(self):
        import datetime
        return int((datetime.date.today() - self.birthday).days / 365.25)
