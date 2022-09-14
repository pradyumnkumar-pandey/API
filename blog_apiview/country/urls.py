from django.contrib import admin
from django.urls import path,include
from .views import CountryView,StateView,CityView

urlpatterns=[
    path('country/',CountryView.as_view()),
    path('country/<int:pk>',CountryView.as_view()),
    path('state/',StateView.as_view()),
    path('state/<int:pk>',StateView.as_view()),
    path('city/',CityView.as_view()),
    path('city/<int:pk>',CityView.as_view())
]