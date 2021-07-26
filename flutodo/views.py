from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

from flutodo_api.models import ToDoItem
from flutodo_api.serializers import ToDoItemSerializer, ToDoItemCreateSerializer


class ToDoList(LoginRequiredMixin, APIView):
    login_url = "accounts/login"
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "todo_list.html"
    swagger_schema = None

    def get(self, request, *args, **kwargs):
        queryset = ToDoItem.objects.order_by("id")
        serializer = ToDoItemSerializer
        return Response({"todos": queryset, "serializer": serializer})


class ToDoCreate(LoginRequiredMixin, APIView):
    login_url = "accounts/login"
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "todo_create.html"
    swagger_schema = None

    def get(self, request):
        serializer = ToDoItemCreateSerializer
        return Response({"serializer": serializer})

    def post(self, request):
        serializer = ToDoItemCreateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({"serializer": serializer})
        serializer.save()
        return redirect("todo_list")


class TodoRemove(LoginRequiredMixin, APIView):
    login_url = "accounts/login"
    swagger_schema = None

    def post(self, request, pk):
        """
        Remove object
        """
        todo = get_object_or_404(ToDoItem, pk=pk)
        todo.delete()
        messages.success(
            request, "Todo item {} has been deleted correctly".format(todo.name)
        )
        return redirect("todo_list")


class TodoComplete(LoginRequiredMixin, APIView):
    login_url = "accounts/login"
    swagger_schema = None

    def post(self, request, pk):
        """
        Remove object
        """
        todo = get_object_or_404(ToDoItem, pk=pk)
        todo.is_complete = True
        todo.save()
        return redirect("todo_list")


class TodoUncomplete(LoginRequiredMixin, APIView):
    login_url = "accounts/login"
    swagger_schema = None

    def post(self, request, pk):
        """
        Remove object
        """
        todo = get_object_or_404(ToDoItem, pk=pk)
        todo.is_complete = False
        todo.save()
        return redirect("todo_list")
