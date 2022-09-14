from .models import *
from rest_framework import serializers
from rest_framework.serializers import SerializerMethodField

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model=City
        fields=['name']

class StateSerializer(serializers.ModelSerializer):
    city=SerializerMethodField()
    
    class Meta:
        model=State
        fields=['id','name','city']
    
    def get_city(self,obj):
        city_list=City.objects.filter(state=obj.id).all()
        serializer=CitySerializer(city_list,many=True)
        return serializer.data

class CountrySerializer(serializers.ModelSerializer):
    state=SerializerMethodField()
    
    class Meta:
        model= Country
        fields=["id",'name','state']
    
    def get_state(self,obj):
        state_list=State.objects.filter(country=obj.id).all()
        serializer=StateSerializer(state_list,many=True)
        return serializer.data

class CountrysSerializer(serializers.ModelSerializer):
    class Meta:
        model=Country
        fields=['name']

class StatesSerializer(serializers.ModelSerializer):
    city=SerializerMethodField()
    country=CountrysSerializer()
    class Meta:
        model=State
        fields=['id','name','country','city']
    def get_city(self,obj):
        city_list=City.objects.filter(state=obj.id).all()
        serializer=CitySerializer(city_list,many=True)
        return serializer.data
    def get_country(self,obj):
        country_list=Country.objects.filter(id=obj.country).all()
        serializer=CountrysSerializer(country_list,many=True)
        return serializer.data

class CitysSerializer(serializers.ModelSerializer):
    class Meta:
        model=City
        fields='__all__'


class StateSerializer2(serializers.ModelSerializer):
    class Meta:
        model=State
        fields='_all__'
        
class CityStateSerializer(serializers.ModelSerializer):
    state=serializers.StringRelatedField()
    class Meta:
        model=City
        fields=['id','name','state']
