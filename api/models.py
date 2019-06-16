"""
All your application modules and serializers are going to be declared inside this file
"""
from rest_framework import serializers
from django.db import models

class User(models.Model):
    name = models.CharField(max_length=150, primary_key=True)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model= User
        fields = ('user_name')

class Task(models.Model):
    user_name = models.ForeignKey('User', on_delete=models.CASCADE)
    label = models.CharField(max_length=150, default='')
    done = models.BooleanField(default=False)

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('label', 'done')