from django.contrib.auth.models import User
from Task.models import Task
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "email", "password", "url"]


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ["content", "created_on"]
