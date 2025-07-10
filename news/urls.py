from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'news',views.NewsViewSets,basename='news')

urlpatterns = [
    path('',include(router.urls))
]
