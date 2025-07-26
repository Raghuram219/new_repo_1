from django.contrib import admin
from app.models import *

class StudentAdmin(admin.ModelAdmin):
    class Meta:
        model=Student
        fields='__all__'

admin.site.register(Student,StudentAdmin)
admin.site.register(CustomUser)
