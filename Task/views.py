from django.contrib.auth.models import User
from rest_framework import request, status
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import viewsets, permissions
from rest_framework.generics import CreateAPIView
from Task.models import Task
from Task.serializers import UserSerializer, TaskSerializer

# Create your views here.
class CreateUserViewSet(viewsets.ViewSet):
    def create(self, request):
        print(request.data)
        user = User(
            username=request.data.get("username"),
            email=request.data.get("email"),
            first_name=request.data.get("first_name"),
            last_name=request.data.get("last_name"),
            password=request.data.get("password"),
        )
        print("1", user)
        user = User.objects.get_or_create(user)
        print("2", user)
        serializer = UserSerializer(user)
        return Response(serializer.data)


class ListUserViewSet(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request):
        serializer = UserSerializer(request.user, context={"request": request})
        return Response(serializer.data)


class ListTaskViewSet(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request):
        queryset = Task.objects.filter(created_by=request.user)
        serializer = TaskSerializer(queryset, many=True, context={"request": request})
        return Response(serializer.data)


class CreateTaskViewSet(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request):
        try:
            print(request.data)
            task = Task(content=request.data.get("content"), created_by=request.user)
            print("1", task)
            task = Task.objects.create(task)
            print("2", task)
            serializer = TaskSerializer(task, context={"request": request})
            return Response(serializer.data)
        except Exception as exc:
            return Response(
                {"message": exc.__str__()}, status=status.HTTP_400_BAD_REQUEST
            )
