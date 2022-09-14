from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *
from rest_framework.response import Response
# Create your views here.

class PersonListView(generics.ListAPIView):
    queryset=Person.objects.all()
    serializer_class=PersonSerializer

class PersonCreateView(generics.CreateAPIView):
    queryset=Person.objects.all()
    serializer_class=PersonSerializer

class PersonListCreateView(generics.ListAPIView,generics.CreateAPIView):
    queryset=Person.objects.all()
    serializer_class=PersonSerializer

class PersonRetrieveView(generics.RetrieveAPIView):
    queryset=Person.objects.all()
    serializer_class=PersonSerializer
    lookup_field='id'

class PersonUpdateView(generics.UpdateAPIView):
    queryset=Person.objects.all()
    serializer_class=PersonSerializer

class PersonDestroyView(generics.DestroyAPIView):
    queryset=Person.objects.all()
    serializer_class=PersonSerializer

class PersonRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset=Person.objects.all()
    serializer_class=PersonSerializer

