from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from . import views

schema_view = get_schema_view(
   openapi.Info(
      title="Flutodo REST API",
      default_version='v1',
      description="Dummy description",
      contact=openapi.Contact(email="oriolromanipicas"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('', views.ToDoItemList.as_view()),
    path('create', views.TodoItemCreate.as_view()),
    path('<int:pk>', views.ToDoItemDetail.as_view()),
    path('accounts/', include('rest_registration.api.urls')),
    path('playground/', schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),
    path('docs/', schema_view.with_ui('redoc', cache_timeout=0),
         name='schema-redoc'),
]
