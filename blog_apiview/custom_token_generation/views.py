from django.shortcuts import render
from rest_framework.response import Response
from django.http import Http404,HttpResponseRedirect
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from app.EmailBackend import EmailBackend
from django.shortcuts import redirect
from django.contrib.auth import login
from rest_framework_simplejwt.tokens import RefreshToken
from django.conf import settings
import jwt
from .Token_Generation import get_access_token,get_refresh_token
# Create your views here.

class GenerateToken(APIView):
    def get(self,request):
        return Response({'Message':"Enter Email and Password To Generate Access and Refresh Tokens"})
    
    def post(self,request):
        email=request.data.get('email')
        password=request.data.get('password')
        if not email or not password:
            return Response({"Error":"Email or Password Cannot be Blank"})
        else:
            user=EmailBackend.authenticate(request,email=email,password=password)
            if not user:
                return Response({"Error":"No Users Found For Given Credentials"})
            else:
                access_token=get_access_token(user)
                refresh_token=get_refresh_token(user)
                data={'Email':email,'Role':user.role.name,'access':str(access_token),'refresh':str(refresh_token)}
                return Response(data)
        
