import json
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import Task, TaskSerializer, User


class TaskView(APIView):
    def get(self, request, user_name):
        tasks = Task.objects.filter(user_name=user_name)
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, user_name):
        newUser = User(name=user_name)
        newUser.save()
        response = {"result": "ok"}
        return Response(response, status=status.HTTP_200_OK)

    def put(self, request, user_name):
        tasks = Task.objects.filter(user_name=user_name)
        tasks.delete()
        user = User.objects.get(name=user_name)
        newList = json.loads(request.body)
        for task in newList:
            newTask = Task(user_name=user, label= task["label"], done=task["done"])
            newTask.save()
        response = {"result": "ok"}
        return Response(response, status=status.HTTP_200_OK)

    def delete(self, request, user_name):
        user = User.objects.get(name=user_name)
        user.delete()
        response = {"result": "ok"}
        return Response(response, status=status.HTTP_204_NO_CONTENT)