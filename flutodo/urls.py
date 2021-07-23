from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.ToDoList.as_view(), name="todo_list"),
    path('<int:pk>', views.ToDoDetail.as_view(), name="todo_detail"),
]
