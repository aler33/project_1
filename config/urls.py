from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from employees.views import EmployeesModelViewSet, EmployeesDepartmentModelViewSet
from department.views import DepartmentModelViewSet


router = DefaultRouter()
router.register('employ-depart', EmployeesDepartmentModelViewSet)
router.register('department', DepartmentModelViewSet)
router.register('employees', EmployeesModelViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
