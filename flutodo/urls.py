from django.urls import path
from . import views

urlpatterns = [
    path('', views.ToDoItemListCreate.as_view()),
    path('<int:pk>', views.ToDoItemDetail.as_view()),

]