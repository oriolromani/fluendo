from rest_framework import permissions
from .models import ToDoItem
from .serializers import ToDoItemSerializer
from rest_framework import generics


class ToDoItemListCreate(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = ToDoItem.objects.all()
    serializer_class = ToDoItemSerializer


class ToDoItemDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = ToDoItem.objects.all()
    serializer_class = ToDoItemSerializer
