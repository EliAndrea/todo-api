from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import Task, TaskSerializer


class TaskView(APIView):
    def get(self, request, user_name):
        tasks = Task.objects.filter(user_name=user_name)
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    def post(self, request, user_name):
        new_user = Task(user_name=user_name, label="run", done=False)
        new_user.save()
        serializer = TaskSerializer(new_user, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self,request, user_name):
        tasks = Task.objects.filter(user_name=user_name)
        tasks.delete()
        print(request.data)
        tasks_list = request.data["list"]
        for task in tasks_list:
            new_task = Task(user_name=user_name, label= task["label"], done=False)
            new_task.save()
        new_tasks = Task.objects.filter(user_name=user_name)
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, user_name):
        task = Task.objects.filter(user_name=user_name)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)