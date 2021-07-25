from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.ToDoItemList.as_view()),
    path('create', views.TodoItemCreate.as_view()),
    path('<int:pk>', views.ToDoItemDetail.as_view()),
    path('accounts/', include('rest_registration.api.urls')),
]
