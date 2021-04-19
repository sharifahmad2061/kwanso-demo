from django.contrib.auth.models import User
from rest_framework import request, status
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import viewsets, permissions
from rest_framework.generics import CreateAPIView
from Task.models import Task
from Task.serializers import UserSerializer, TaskSerializer

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class CreateUser(CreateAPIView):
    serializer_class = UserSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request):
        print(self.request.user)
        queryset = Task.objects.filter(created_by=request.user)
        serializer = TaskSerializer(queryset, many=True, context={"request": request})
        return Response(serializer.data)


class ListTaskViewSet(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request):
        queryset = Task.objects.filter(created_by=self.request.user)
        serializer = TaskSerializer(queryset, many=True, context={"request": request})
        return Response(serializer.data)


class CreateTaskViewSet(viewsets.ViewSet):
    http_method_names = ["POST"]
    queryset = Task.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request):
        try:
            print(request.data)
            task = Task(
                content=request.data.get("content"), created_by=self.request.user
            )
            print("1", task)
            task = Task.objects.create(task)
            print("2", task)
            serializer = TaskSerializer(task, context={"request": request})
            return Response(serializer.data)
        except Exception as exc:
            return Response(
                {"message": exc.__str__()}, status=status.HTTP_400_BAD_REQUEST
            )
