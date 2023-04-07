from django.db.models import Count, Sum
from rest_framework.viewsets import ModelViewSet
from .models import Department
from .serializers import DepartmentSerializer, DepartmentMoreSerializer
from rest_framework import permissions


class DepartmentModelViewSet(ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    filterset_fields = ['id', 'name']
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        return Department.objects.annotate(total_employees=Count('employee'),
                                           total_salary=Sum('employee__salary')
                                           )

    def get_serializer_class(self):
        if self.request.method in ['POST']:
            return DepartmentSerializer
        return DepartmentMoreSerializer
