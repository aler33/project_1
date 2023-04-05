from django.contrib import admin
from department import models as department_models
from authapp import models as authapp_models
from employees import models as employees_models


# admin.site.register(department_models.Department)
admin.site.register(authapp_models.CustomUser)
# admin.site.register(employees_models.Employee)


@admin.register(employees_models.Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id', 'last_name', 'first_name', 'sur_name', 'job_title', 'photo', 'salary', 'birthday', 'get_department_name']
    list_filter = ['last_name', 'first_name', 'job_title', 'salary', 'department_id']

    def get_department_name(self, obj):
        return obj.department_id.name

    get_department_name.short_description = ('Department')


@admin.register(department_models.Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'get_employees_name']

    def get_employees_name(self, obj):
        # return f'{obj.director.last_name} {obj.director.first_name}'
        if obj.director:
            return f'{obj.director.last_name} {obj.director.first_name}'
        else:
            return obj.director

    get_employees_name.short_description = ('Director')
