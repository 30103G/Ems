from django.contrib import admin

# Register your models here.
from . models import *

admin.site.register(Faculty)
admin.site.register(Student)
admin.site.register(Exam)
admin.site.register(Question)
admin.site.register(AssementAnswer)
admin.site.register(Assesment)
