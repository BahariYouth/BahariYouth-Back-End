from rest_framework.routers import DefaultRouter
from django.urls import path,include
from . import views

router = DefaultRouter()
router.register(r'activity',views.ActivityViewSets,basename='activiry')


urlpatterns = [
    path('',include(router.urls)),
]
