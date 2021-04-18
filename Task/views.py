from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import viewsets, permissions
from Task.models import Task
from Task.serializers import UserSerializer, TaskSerializer

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request):
        print(self.request.user)
        queryset = Task.objects.filter(created_by=request.user)
        serializer = TaskSerializer(queryset, many=True, context={"request": request})
        return Response(serializer.data)