from django.shortcuts import render
from rest_framework.response import Response
from django.http import Http404,HttpResponseRedirect
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from app.EmailBackend import EmailBackend
from django.shortcuts import redirect
from django.contrib.auth import login
from rest_framework_simplejwt.tokens import RefreshToken
from django.conf import settings
import jwt
from django.utils.decorators import decorator_from_middleware_with_args
from .middleware import UserAgeVerification
# Create your views here.

class UserRegistrationView(APIView):
    def get(self,request):
        return Response({"message":"""please enter details as follows :{'first_name': 'First name','last_name': 'Last name','email': 'email@gmail.com','password':'XXXXX','role': {'role_user': 1/2}"""})
    def post(self,request):
        serializer_user=UserRegistrationSerializer(data=request.data)
        
        if serializer_user.is_valid():
            #breakpoint()
            try:
                serializer_user.save()
            except AssertionError:
                return Response('You Entered Some Wrong Data, Plase Try Again')
            else:
                return Response(serializer_user.data)
        else:
            return Response(serializer_user.errors)

class UserLoginView(APIView):
    def get(self,request):
        return Response({"Login Page":"Please Enter Email and Password To Login"})
    #@decorator_from_middleware_with_args(UserAgeVerification)
    def post(self,request):
        email=request.data.get('email')
        password=request.data.get('password')
        if not email or not password:
            return Response({'Error':'Email or Password Cannot be Blank'})
        else:
            user=EmailBackend.authenticate(request,email=email,password=password)
            if user:
                if user.role_id==1:
                    refresh_token=RefreshToken.for_user(user)
                    #print(type(refresh_token),'@@@@')
                    #refresh_token['email']=user.email
                    data={'email':str(email),'role':str(user.role.name),'refresh': str(refresh_token),'access': str(refresh_token.  access_token)}
                    #print('iat=',refresh_token['iat'])
                    #print('exp=',refresh_token['exp'])
                    #print('duration=',refresh_token['exp']-refresh_token['iat'])
                    #print('user token exp=',user.token,'!!!!!!!!!')
                    login(request,user,backend="app.Emailbackend.EmailBackend")
                    #print(request.user,'$$$$$$$$$$$$$')
                    return Response(data)
                else:
                    if user.is_active==False:
                        return Response({'Error':'You Cannot Login, Contact Admin'})
                    else:
                        refresh_token=RefreshToken.for_user(user)
                        data={"Success":"User Page",'email':str(email),'role':str(user.role.name),'refresh': str(refresh_token),'access': str(refresh_token.  access_token)}
                        login(request,user,backend='app.Emailbackend.EmailBackend')
                        return Response(data)
            else:
                return Response({"Error":"User Not Found for Given Credentials"})


class UserStatusUpdateView(APIView):
    permission_classes=(IsAuthenticated,)
    def get_user_list(self,pk):
        try:
            obj=CustomUser.objects.get(id=pk)
        except CustomUser.DoesNotExist:
            raise Http404
        else:
            return obj
    def get(self,request,pk=None):
        if pk is None:
            obj=CustomUser.objects.filter(role_id=2).all()
            serializer=UserListSerializer(obj,many=True)
            return Response(serializer.data)
        else:
            obj=self.get_user_list(pk)
            serializer=UserListSerializer(obj)
            return Response(serializer.data)
            
    def put(self,request,pk=None):
        if pk is None:
            return Response({'Error':"Primary Key Not Provided"})
        else:
            email=request.data.get('email')
            is_active=request.data.get('is_active')
            if not email or not is_active:
                return Response({'Error':"Email or IsActive Cannot Be Blank"})
            else:
                user=self.get_user_list(pk)
                if is_active=="True" or is_active=="1":
                    user.is_active=True
                    user.save()
                elif is_active=="False" or is_active=="0":
                    user.is_active=False
                    user.save()
                else:
                    return Response({'Error':"Enter Correct Value in IsActive Field"})
                return Response(UserListSerializer(user).data)
    
    def delete(self,request,pk=None):
        if pk is None:
            return Response({'Error':'Primary Key Not Provided'})
        else:
            user=self.get_user_list(pk)
            user.is_deleted=True
            user.is_active=False
            user.save()
            return Response({'Success':"User deleted Successfully"})


class RenewJWTToken(APIView):
    def get(self,request):
        return Response({'Message':"Enter Access Token and Refresh Token To Get New Access and Refresh Token"})
    
    def post(self,request):
        access=request.data.get('access')
        refresh=request.data.get('refresh')
        if not refresh or not access:
            return Response({'Error':"Refresh or Access Cannot Be Blank"})
        else:
        #access=RefreshToken(access)
            try:
                payload_refresh=jwt.decode(refresh, settings.SECRET_KEY, algorithms=["HS256"])
            except jwt.ExpiredSignatureError:
                return Response({"Error":"Refresh Token Expired Please Login Again"})
            else:
                try:
                    user=CustomUser.objects.get(id=payload_refresh.get('user_id'))
                except CustomUser.DoesNotExist:
                    return Response({'Error':"Related User Does Not Exists"})
                else:
                    refresh_token=RefreshToken.for_user(user)
                    data={'email':user.email,'Role':user.role.name,'Access Token': str(refresh_token.access_token),'Refresh Token': str(refresh_token)}
                    return Response(data)
