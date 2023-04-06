from django.contrib import admin
from django.urls import include, path, re_path
from rest_framework.routers import DefaultRouter
from employees.views import EmployeesModelViewSet, EmployeesDepartmentModelViewSet
from department.views import DepartmentModelViewSet
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title='Project',
        default_version='1.0',
        description='Documentation to project',
    ),
    public=True,
)


router = DefaultRouter()
router.register('department', DepartmentModelViewSet)
router.register('employ-depart', EmployeesDepartmentModelViewSet)
router.register('employees', EmployeesModelViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path("auth/", include("rest_framework.urls")),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
