from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from addresses import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('addresses/', views.address_list),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('addresses/<int:pk>/', views.address),
    path('login/', views.login)
]