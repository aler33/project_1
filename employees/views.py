from django.shortcuts import render, get_object_or_404
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import Employee
from .serializers import EmployeesSerializer, EmployeesPostSerializer


class EmployeesModelViewSet(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeesSerializer
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    filterset_fields = ['last_name', 'department_id']

    def get_serializer_class(self):
        if self.request.method in ['POST']:
            return EmployeesPostSerializer
        return EmployeesSerializer


class EmployeesDepartmentModelViewSet(ModelViewSet):
    queryset = Employee.objects.order_by('department_id')
    serializer_class = EmployeesSerializer
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]

    def get_serializer_class(self):
        if self.request.method in ['POST']:
            return EmployeesPostSerializer
        return EmployeesSerializer
