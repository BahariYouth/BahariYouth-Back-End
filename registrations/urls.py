from rest_framework.routers import DefaultRouter
from django.urls import path,include
from .views import EventRegistrationViewSet,ActivitiesRegistrationViewSet

router = DefaultRouter()
router.register(r'event-registration', EventRegistrationViewSet, basename='event-registration')
router.register(r'activity-registration', ActivitiesRegistrationViewSet, basename='activity-registration')

urlpatterns = [
    path('',include(router.urls))
]
