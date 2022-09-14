from django.contrib import admin
from django.urls import path,include
from .views import *
urlpatterns=[
    path('person_list/',PersonListView.as_view()),
    path('person_create/',PersonCreateView.as_view()),
    path('person_list_create/',PersonListCreateView.as_view()),
    path('person_retrieve/',PersonListView.as_view()),
    path('person_retrieve/<id>',PersonRetrieveView.as_view()),
    path('person_update',PersonListView.as_view()),
    path('person_update/<pk>',PersonUpdateView.as_view()),
    path('person_delete/<pk>',PersonDestroyView.as_view()),
    path('person_operations/<pk>',PersonRetrieveUpdateDestroy.as_view()),
    
]