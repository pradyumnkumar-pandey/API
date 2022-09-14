from django.contrib import admin
from django.urls import path
from .views import GenerateToken
urlpatterns=[
    path('generate_token/',GenerateToken.as_view())
]