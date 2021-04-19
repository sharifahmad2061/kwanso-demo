from django.contrib.auth.models import User
from django.db.models import query
from rest_framework import status
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from Task.models import Task
from Task.serializers import UserSerializer, TaskSerializer

# Create your views here.
class UsersViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer