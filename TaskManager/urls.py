"""TaskManager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView
from Task.views import (
    CreateUserViewSet,
    RetrieveUserViewSet,
    CreateTaskViewSet,
    ListTaskViewSet,
    UsersViewSet,
    TaskViewSet,
)


router = routers.DefaultRouter()
# router.register("register", CreateUserViewSet, basename="registeruser")

# router.register("user", RetrieveUserViewSet, basename="showuser")
# router.register("create-task", CreateTaskViewSet, basename="createtask")
# router.register("list-tasks", ListTaskViewSet, basename="listtask")
router.register("user", UsersViewSet)
user_create = UsersViewSet.as_view({"post": "create"})
user_list = UsersViewSet.as_view({"get": "list"})
task_list = TaskViewSet.as_view({"get": "list"})
task_create = TaskViewSet.as_view({"post": "create"})

urlpatterns = [
    path("", include(router.urls)),
    path("auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("admin/", admin.site.urls),
    path("register/", user_create, name="user_register"),
    path("user/", user_list, name="current_user"),
    path("create-task/", task_create, name="task_create"),
    path("list-task/", task_list, name="task_list"),
]
