from rest_framework.routers import DefaultRouter
from django.urls import path,include
from .views import EventRegistrationViewSet,ActivitiesRegistrationViewSet

router = DefaultRouter()
router.register(r'register-event',EventRegistrationViewSet,basename='rigester-event')
router.register(r'register-activity',ActivitiesRegistrationViewSet,basename='activity-event')

urlpatterns = [
    path('',include(router.urls))
]
