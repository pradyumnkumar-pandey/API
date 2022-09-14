from django.shortcuts import render
from rest_framework.response import Response
from django.http import Http404
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
# Create your views here.


class CountryView(APIView):
    
    permission_classes=(IsAuthenticated,)
    def get_country_detail(self,pk):
        try:
            obj=Country.objects.get(id=pk)
        except Country.DoesNotExist:
            raise Http404
        else:
            return obj
    
    def get(self,request,pk=None):
        if pk is None:
            print(request.user.is_authenticated,'&&&&&&&&&&&&&&&&&&&&&&&&&&&')
            obj=Country.objects.all()
            serializer_country=CountrySerializer(obj,many=True)
            return Response(serializer_country.data)
        else:
            obj=self.get_country_detail(pk)
            serializer_country=CountrySerializer(obj)
            return Response(serializer_country.data)
    
    def post(self,request):
        serializer_country=CountrySerializer(data=request.data)
        if serializer_country.is_valid():
            serializer_country.save()
            return Response(serializer_country.data)
        else:
            return Response(serializer_country.errors)
    
    def put(self,request,pk=None):
        if pk is None:
            return Response({'message':'Primary Key Not Provided'})
        else:
            obj=self.get_country_detail(pk)
            serializer_country=CountrySerializer(obj,data=request.data)
            if serializer_country.is_valid():
                serializer_country.save()
                return Response(serializer_country.data)
            else:
                return Response(serializer_country.errors)
    
    def delete(self,request,pk=None):
        if pk is None:
            return Response({'Error':'Primary Key Not Provided'})
        else:
            obj=self.get_country_detail(pk)
            obj.delete()
            return Response({'message':'Country Deleted Successfully.'})


        
class StateView(APIView):
    permission_classes=(IsAuthenticated,)
    def get_state_detail(self,pk):
        try:
            obj=State.objects.get(id=pk)
        except State.DoesNotExist:
            raise Http404
        else:
            return obj
    
    def get(self,request,pk=None):
        if pk is None:
            obj=State.objects.all()
            serializer_state=StatesSerializer(obj,many=True)
            return Response(serializer_state.data)
        else:
            obj=self.get_state_detail(pk)
            serializer_state=StatesSerializer(obj)
            return Response(serializer_state.data)
    
    def post(self,request):
        serializer=StateSerializer2(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    
    def put(self,request,pk=None):
        if pk is None:
            return Response({'message':"Primary Key Not Provided"})
        else:
            obj=self.get_state_detail(pk)
            serializer=StateSerializer(obj,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors)
    
    def delete(self,request,pk=None):
        if pk is None:
            return Response({'Error':'Primary Key Not Provided'})
        else:
            obj=self.get_state_detail(pk)
            obj.delete()
            return Response({'message':'State Successfully Deleted.'})

class CityView(APIView):
    permission_classes=(IsAuthenticated,)
    def get_city_details(self,pk):
        try:
            obj=City.objects.get(id=pk)
        except City.DoesNotExist:
            raise Http404
        else:
            return obj
    
    def get(self,request,pk=None):
        if pk is None:
            obj=City.objects.all()
            serializer_city=CityStateSerializer(obj,many=True)
            return Response(serializer_city.data)
        else:
            obj=self.get_city_details(pk)
            serializer_city=CitySerializer(obj)
            return Response(serializer_city.data)
    
    def post(self,request):
        serializer=CityStateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    
    def put(self,request,pk=None):
        if pk is None:
            return Response({'Message':'Primary Key Not Provided'})
        else:
            obj=self.get_city_details(pk)
            serializer=CitySerializer(obj,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors)
    
    def delete(self,request,pk=None):
        if pk is None:
            return Response({'Error':'Primary Key Not Provided'})
        else:
            obj=self.get_city_details(pk)
            obj.delete()
            return Response({'message':'City Successfully Deleted'})