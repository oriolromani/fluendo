from rest_framework import serializers
from .models import ToDoItem


class ToDoItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDoItem
        fields = ("id", "name", "is_complete")


class ToDoItemCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDoItem
        fields = ("name",)
