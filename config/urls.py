from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from employees.views import EmployeesModelViewSet


router = DefaultRouter()
# router.register("department", departmentModelViewSet)
router.register("employees", EmployeesModelViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", include(router.urls)),
]
