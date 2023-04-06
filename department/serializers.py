from rest_framework.serializers import ModelSerializer, IntegerField
from .models import Department


class DepartmentSerializer(ModelSerializer):

    class Meta:
        model = Department
        # fields = "__all__"
        fields = (
            'id',
            'name',
            'director',
        )


class DepartmentMoreSerializer(ModelSerializer):
    total_employees = IntegerField()
    class Meta:
        model = Department
        # fields = "__all__"
        fields = (
            'id',
            'name',
            'director',
            'total_employees',
        )
