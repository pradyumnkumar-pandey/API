from .models import Role
from app.models import CustomUser
from rest_framework import serializers
from rest_framework.serializers import SerializerMethodField
from django.contrib.auth.hashers import make_password

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model=Role
        fields=['role_user']

class UserRegistrationSerializer(serializers.ModelSerializer):
    first_name=serializers.CharField()
    last_name=serializers.CharField()
    role=RoleSerializer()
    class Meta:
        model=CustomUser
        fields=['first_name','last_name','email','password','role']
    
    def create(self,validated_data):
        role=validated_data['role']
        role=role['role_user']
        if role==1:
            user=CustomUser.objects.create(email=validated_data['email'],first_name=validated_data['first_name'],last_name=validated_data['last_name'],role_id=role)
            user.set_password(validated_data['password'])
            user.save()
            return user
        elif role==2:
            user=CustomUser.objects.create(email=validated_data['email'],first_name=validated_data['first_name'],last_name=validated_data['last_name'],role_id=role,is_active=False)
            user.set_password(validated_data['password'])
            user.save()
            return user
        else:
            return None

class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model=CustomUser
        fields=['email','password']


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model=CustomUser
        fields=['id','first_name','last_name','email','role','is_active']