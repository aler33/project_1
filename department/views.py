from django.db.models import Count
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Department, Employee
from .serializers import DepartmentSerializer, DepartmentMoreSerializer
from rest_framework import permissions


class DepartmentModelViewSet(ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentMoreSerializer
    filterset_fields = ['id', 'name']
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        # return Department.objects.annotate(total_employees=Count('employee'))
        return Department.objects.annotate(total_employees=Count('employee'))


class DepartmentListViewSet(ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

    def get_queryset(self):
        return Employee.objects.annotate(total_employees=Count('salary'))
