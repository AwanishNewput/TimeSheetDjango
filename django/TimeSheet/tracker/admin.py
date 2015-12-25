from django.contrib import admin

# Register your models here.
from .models import EmployeeDetail


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ["user_id" , "created" , "updated"]

    class Meta:
        model = EmployeeDetail

admin.site.register(EmployeeDetail,EmployeeAdmin)
