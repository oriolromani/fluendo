from django.contrib import admin

from .models import ToDoItem


@admin.register(ToDoItem)
class TodoItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_complete')
