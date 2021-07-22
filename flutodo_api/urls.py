from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.ToDoItemListCreate.as_view()),
    path('<int:pk>', views.ToDoItemDetail.as_view()),
    path('accounts/', include('rest_registration.api.urls')),
]
