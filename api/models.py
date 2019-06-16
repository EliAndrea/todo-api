"""
All your application modules and serializers are going to be declared inside this file
"""
from rest_framework import serializers
from django.db import models

class Task(models.Model):
    user_name = models.CharField(max_length=150, default='')
    label = models.CharField(max_length=150, default='')
    done = models.BooleanField(default=False)

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('user_name', 'label', 'done')