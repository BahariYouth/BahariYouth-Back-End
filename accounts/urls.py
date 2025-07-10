from rest_framework.routers import DefaultRouter
from django.urls import path,include
from .views import signup,login


urlpatterns = [
    path('signup/',signup,name='sign-up'),
    path('login/',login,name='log-in')
]
