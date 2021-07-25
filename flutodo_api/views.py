from rest_framework import permissions
from .models import ToDoItem
from .serializers import ToDoItemSerializer, ToDoItemCreateSerializer
from rest_framework import generics


class ToDoItemList(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = ToDoItem.objects.all()
    serializer_class = ToDoItemSerializer


class TodoItemCreate(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = ToDoItem.objects.all()
    serializer_class = ToDoItemCreateSerializer


class ToDoItemDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = ToDoItem.objects.all()
    serializer_class = ToDoItemSerializer
