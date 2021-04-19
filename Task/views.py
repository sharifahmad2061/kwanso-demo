from django.contrib.auth.models import User
from django.db.models import query
from rest_framework import status
from rest_framework import viewsets, permissions
from rest_framework import request
from rest_framework.decorators import action
from rest_framework.response import Response
from Task.models import Task
from Task.serializers import UserSerializer, TaskSerializer

# Create your views here.
class UsersViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes_by_action = {
        "create": [permissions.AllowAny],
        "list": [permissions.IsAuthenticated],
        "destroy": [permissions.IsAdminUser],
    }

    def list(self, request):
        try:
            serializer = UserSerializer(self.request.user)
            return Response(serializer.data)
        except Exception as exc:
            return Response(
                {"message": exc.__str__()}, status=status.HTTP_400_BAD_REQUEST
            )


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]