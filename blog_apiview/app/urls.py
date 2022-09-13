from django.contrib import admin
from django.urls import path,include
from rest_framework_simplejwt import views as jwt_views
from .views import BlogView,AuthorView,AuthorBlogView,AccountView,UserLoginView,UserLoginView2,UpdateUserStatus

urlpatterns = [
    path('blog/', BlogView.as_view()),
    path('blog/<int:pk>',BlogView.as_view()),
    path('author/',AuthorView.as_view()),
    path('author/<int:pk>',AuthorView.as_view()),
    path('author/list/<int:id>',AuthorBlogView.as_view()),
    path('token/',jwt_views.TokenObtainPairView.as_view(),name ='token_obtain_pair'),
    path('token/refresh/',jwt_views.TokenRefreshView.as_view(),name ='token_refresh'),
    path('login/',UserLoginView.as_view()),
    path('login2/',UserLoginView2.as_view()),
    path('account/',AccountView.as_view()),
    path('update_status/',UpdateUserStatus.as_view())
]