from django.contrib import admin
from Task.models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ("content", "created_on", "created_by")


# Register your models here.
admin.site.register(Task, TaskAdmin)