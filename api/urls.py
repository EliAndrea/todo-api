from django.contrib import admin
from django.urls import path, include
from api import views
urlpatterns = [
    path('user/<str:user_name>', views.TaskView.as_view(), name='user'),
]