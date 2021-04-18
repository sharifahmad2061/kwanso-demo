from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Task(models.Model):
    content = models.TextField(verbose_name="task content", max_length=128)
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)