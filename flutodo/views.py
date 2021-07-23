from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import redirect, get_object_or_404
from rest_framework import permissions
from django.contrib.auth.mixins import LoginRequiredMixin

from flutodo_api.models import ToDoItem
from flutodo_api.serializers import ToDoItemSerializer


class ToDoList(LoginRequiredMixin, APIView):
    login_url = "api/accounts/login"
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "todo_list.html"

    def get(self, request):
        queryset = ToDoItem.objects.all()
        serializer = ToDoItemSerializer
        return Response({"todos": queryset,
                         "serializer": serializer})

    def post(self, request):
        serializer = ToDoItemSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer})
        serializer.save()
        return redirect("todo_list")


class ToDoDetail(LoginRequiredMixin, APIView):
    login_url = "api/accounts/login"
    permission_classes = [permissions.IsAuthenticated]
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "todo_detail.html"

    def get(self, request, pk):
        todo = get_object_or_404(ToDoItem, pk=pk)
        serializer = ToDoItemSerializer(todo)
        return Response({"serializer": serializer, "todo": todo})

    def post(self, request, pk):
        todo = get_object_or_404(ToDoItem, pk=pk)
        serializer = ToDoItemSerializer(todo, data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer, 'todo': todo})
        serializer.save()
        return redirect('todo_detail', pk=pk)
