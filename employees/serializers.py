from rest_framework.serializers import ModelSerializer
from .models import Employee


class EmployeesSerializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = (
            'last_name',
            'first_name',
            'sur_name',
            'photo',
            'job_title',
            'salary',
            'age',
            'department_id',
        )


class EmployeesPostSerializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = (
            'last_name',
            'first_name',
            'sur_name',
            'photo',
            'job_title',
            'salary',
            'birthday',
            'department_id',
        )
