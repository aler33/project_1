from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import LimitOffsetPagination
from rest_framework import permissions
from .models import Employee
from .serializers import EmployeesSerializer, EmployeesPostSerializer


class EmployeeLimitOfsetPagination(LimitOffsetPagination):
    default_limit = 5


class EmployeesModelViewSet(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeesSerializer
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    filterset_fields = ['last_name', 'department_id']
    pagination_class = EmployeeLimitOfsetPagination
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method in ['POST']:
            return EmployeesPostSerializer
        return EmployeesSerializer


class EmployeesDepartmentModelViewSet(ModelViewSet):
    queryset = Employee.objects.all().order_by('department_id')
    serializer_class = EmployeesSerializer
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]

    def get_serializer_class(self):
        if self.request.method in ['POST']:
            return EmployeesPostSerializer
        return EmployeesSerializer
