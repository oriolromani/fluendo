from rest_framework import permissions
from .models import ToDoItem
from .serializers import ToDoItemSerializer, ToDoItemCreateSerializer
from rest_framework import generics


class ToDoItemList(generics.ListAPIView):
    """
    Returns a list of all ToDoItems
    """

    permission_classes = [permissions.IsAuthenticated]
    queryset = ToDoItem.objects.order_by("id")
    serializer_class = ToDoItemSerializer


class TodoItemCreate(generics.CreateAPIView):
    """
    Create a ToDoItem
    """

    permission_classes = [permissions.IsAuthenticated]
    queryset = ToDoItem.objects.all()
    serializer_class = ToDoItemCreateSerializer


class ToDoItemDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or remove a ToDoItem
    """

    permission_classes = [permissions.IsAuthenticated]
    queryset = ToDoItem.objects.all()
    serializer_class = ToDoItemSerializer
