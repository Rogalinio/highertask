from django.contrib import admin
from .models import Candidate, Recruter, Task, Grade
# Register your models here.

admin.site.register(Candidate)
admin.site.register(Recruter)
admin.site.register(Task)
admin.site.register(Grade)
