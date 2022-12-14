from django.contrib import admin
from django.urls import path,include

from app.views import UpdateUserStatus
from .views import UserRegistrationView,UserLoginView,UserStatusUpdateView,RenewJWTToken
#from django.contrib.auth.decorators import login_required
urlpatterns=[
    path('user_registration/',UserRegistrationView.as_view()),
    path('user_login/',UserLoginView.as_view(),name='user_login'),
    path('user_status_update/',UserStatusUpdateView.as_view()),
    path('user_status_update/<int:pk>',UserStatusUpdateView.as_view()),
    path('renew_token/',RenewJWTToken.as_view())
]
