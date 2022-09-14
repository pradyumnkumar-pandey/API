from .models import *
from rest_framework import serializers
from rest_framework.serializers import SerializerMethodField
from django.contrib.auth.models import User 
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Author
        fields="__all__"

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model=Blog
        fields=['author','blog_title','blog_description','blog_image']

class AuthorBlogSerializer(serializers.ModelSerializer):
    author=SerializerMethodField()
    
    def get_author(self,obj):
        return obj.author.name
    
    class Meta:
        model=Blog
        fields="__all__"
        #include=['author']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=CustomUser
        fields=['id','email','first_name','last_name','is_deleted']

class LoginUserSerializer(serializers.ModelSerializer):
    class Meta:
        model=CustomUser
        fields=['email','is_active','is_deleted','token']