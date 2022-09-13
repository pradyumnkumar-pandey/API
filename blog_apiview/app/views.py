from django.shortcuts import render
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework.views import APIView
from django.http import Http404,HttpResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication
from django.contrib.auth.decorators import login_required
from .EmailBackend import EmailBackend
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import login
# Create your views here.


class BlogView(APIView):
    permission_classes=(IsAuthenticated,)
    def get_blog_detail(self,pk):
        try:
            return Blog.objects.get(id=pk)
        except Blog.DoesNotExist:
            raise Http404
        
    def get(self,request,pk=None):
        if pk is None:
            obj=Blog.objects.all()
            serializer=BlogSerializer(obj,many=True)
            return Response(serializer.data)
        else:
            obj=self.get_blog_detail(pk)
            serializer=BlogSerializer(obj)
            return Response(serializer.data)
    
    def post(self, request):
        serializer=BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    
    def put(self,request,pk):
        obj=self.get_blog_detail(pk)
        serializer=BlogSerializer(obj,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    
    def delete(self, request,pk):
        obj=self.get_college_detail(pk)
        obj.delete()
        return Response()

class AuthorBlogView(APIView):
    permission_classes=(IsAuthenticated,)
    def get_authorblog_detail(self,id):
        try:
            return Blog.objects.filter(author_id=id)
        except Blog.DoesNotExist:
            raise Http404

    def get(self,request,id):
        obj=self.get_authorblog_detail(id)
        serializer=AuthorBlogSerializer(obj,many=True)
        return Response(serializer.data)

class AuthorView(APIView):
    permission_classes=(IsAuthenticated,)
    def get_author_detail(self,pk):
        try:
            return Author.objects.get(id=pk)
        except Author.DoesNotExist:
            raise Http404
        
    def get(self,request,pk=None):
        if pk is None:
            obj=Author.objects.all()
            serializer=AuthorSerializer(obj,many=True)
            return Response(serializer.data)
        else:
            obj=self.get_author_detail(pk)
            serializer=AuthorSerializer(obj)
            return Response(serializer.data)
    
    def post(self, request):
        serializer=AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    
    def put(self,request,pk):
        obj=self.get_author_detail(pk)
        serializer=AuthorSerializer(obj,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    
    def delete(self, request,pk):
        obj=self.get_author_detail(pk)
        obj.delete()
        return Response()

class UserLoginView(APIView):
    def get(self, request):
        return Response()
    
    def post(self, request):
        email=request.data.get('email')
        password=request.data.get('password')
        if not email or not password:
            return Response('Email Or Password Cannot Be Blank')
        else:
            user = EmailBackend.authenticate(request, email=email, password=password)
            check_user_active = CustomUser.objects.filter(email=email, is_active=False).last()
            if check_user_active:
                return Response('User is In-Active, Please conact support team')
            elif user.is_deleted:
                return Response("User Has Been Deleted, You Cant Login")
            else:
                login(request,user,backend='app.EmailBackend.EmailBackend')
                serializer_class=LoginUserSerializer(user)
                return Response(serializer_class.data)

class UserLoginView2(APIView):
    def get(self, request):
        return Response()
    
    def post(self, request):
        email=request.data.get('email')
        password=request.data.get('password')
        if not email or not password:
            return Response('Email Or Password Cannot Be Blank')
        else:
            user_profile=CustomUser.objects.filter(email=email).last()
            #print(user_profile.is_deleted,'#####################')
            if user_profile.is_deleted == 1:
                return Response("User Has Been Deleted, You Cant Login")
            else:
                user = EmailBackend.authenticate(request, email=email, password=password)
                check_user_active = CustomUser.objects.filter(email=email, is_active=False).last()
                if check_user_active:
                    return Response('User is In-Active, Please conact support team')
                else:
                    #serializer=LoginUserSerializer(user)
                    refresh_token=RefreshToken.for_user(user)
                    login(request,user,backend='app.EmailBackend.EmailBackend')
                    data={'refresh': str(refresh_token),'access': str(refresh_token.access_token)}
                    return Response(data)
        

class AccountView(APIView):
    def get(self,request):
        obj=CustomUser.objects.all()
        serializer=UserSerializer(obj,many=True)
        return Response(serializer.data)

class UpdateUserStatus(APIView):
    def get(self,request):
        return Response()
    def post(self,request):
        email=request.data.get('email')
        is_deleted=request.data.get('is_deleted')
        if email is None or is_deleted is None:
            return Response('Email or Status Cannot be Bank')
        else:
            try:
                user=CustomUser.objects.get(email=email)
            except CustomUser.DoesNotExist:
                return Response('No User Exists for Given Email')
            else:
                user.is_deleted=is_deleted
                #print(type(is_deleted),is_deleted,'@@@@@@@@@@@@@@@@@@@@@@@')
                if is_deleted=="True":
                    user.is_active=False
                    user.save()
                else:
                    user.is_active=True
                    user.save()
                serializer=UserSerializer(user)
                return Response(serializer.data)
