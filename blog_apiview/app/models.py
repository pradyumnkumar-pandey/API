from django.db import models
from django.contrib.auth.models import AbstractUser,UserManager
from django.contrib.auth.hashers import make_password
import jwt
from django.conf import settings
from datetime import datetime,timedelta
from role_app.models import Role
# Create your models here.

class CustomUserManager(UserManager):
    def _create_user(self, email, password, **extra_fields):
        email = self.normalize_email(email)
        user = CustomUser(email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        assert extra_fields["is_staff"]
        assert extra_fields["is_superuser"]
        return self._create_user(email, password, **extra_fields)

class CustomUser(AbstractUser):
    username=None
    email=models.EmailField(unique=True,max_length=100)
    is_deleted=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    role=models.ForeignKey(Role,null=True,blank=True,on_delete=models.DO_NOTHING,related_name="role")
    dob=models.DateField(null=True,blank=True)
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=[]
    objects=CustomUserManager()
    
    @property
    def token(self):
        token=jwt.encode({'email':self.email,'exp':datetime.utcnow()+ timedelta(seconds=40)}, settings.SECRET_KEY,algorithm='HS256')
        return token
    
class Author(models.Model):
    name=models.CharField(max_length=100)
    address=models.CharField(max_length=150)
    email=models.EmailField()
    def __str__(self):
        return self.name

class Blog(models.Model):
    author=models.ForeignKey(Author,on_delete=models.CASCADE,related_name='author')
    blog_title=models.CharField(max_length=100)
    blog_description=models.CharField(max_length=1500)
    blog_image=models.ImageField(upload_to='blog_image')
    created_at=models.DateTimeField(auto_now_add=True)


