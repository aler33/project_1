from django.db import models
from time import time
from pathlib import Path
# from department.models import Department


def employees_photo_path(instance, filename):
    # file will be uploaded to
    #   MEDIA_ROOT / employee_<username> / photo / <filename>
    num = int(time() * 1000)
    suff = Path(filename).suffix
    return 'employee_{0}/photo/{1}'.format(instance.username, f'pic_{num}{suff}')


class Employee(models.Model):
    first_name = models.CharField(max_length=64, blank=False)
    last_name = models.CharField(max_length=64, blank=False)
    sur_name = models.CharField(max_length=64, blank=True)
    photo = models.ImageField(upload_to=employees_photo_path, blank=True, null=True)
    job_title = models.CharField(max_length=64, blank=True)
    salary = models.PositiveIntegerField()
    age = models.PositiveIntegerField(blank=True, null=True)
    department_id = models.ForeignKey('department.Department', on_delete=models.DO_NOTHING)
