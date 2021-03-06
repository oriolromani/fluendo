from django.urls import path
from . import views

urlpatterns = [
    path("", views.ToDoList.as_view(), name="todo_list"),
    path("create", views.ToDoCreate.as_view(), name="todo_create"),
    path("remove/<int:pk>", views.TodoRemove.as_view(), name="todo_remove"),
    path("complete/<int:pk>", views.TodoComplete.as_view(), name="todo_complete"),
    path("uncomplete/<int:pk>", views.TodoUncomplete.as_view(), name="todo_uncomplete"),
]
