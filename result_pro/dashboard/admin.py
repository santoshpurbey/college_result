from django.contrib import admin

# Register your models here.
from .models import ManageStudent,  Program,Course, ManageTeacher


admin.site.register(Program)
admin.site.register(Course)
admin.site.register(ManageTeacher)
admin.site.register(ManageStudent)