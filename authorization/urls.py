from django.conf.urls import url
from django.urls import path, include
from .api import RegisterApi
from django.contrib import admin
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('api/register', RegisterApi.as_view()),
]

## wersja z filmiku
# from django.urls import path
# from django.conf.urls import include
# from rest_framework import routers
#
# router = routers.DefaultRouter()
#
# urlpatterns = [
#     path('', include(router.urls)),
# ]
