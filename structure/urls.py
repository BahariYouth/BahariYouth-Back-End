from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register(r'governorate',views.GovernorateViewSet,basename='governorate')
router.register(r'Department',views.DepartmentViewSet,basename='Department')
router.register(r'Branch',views.BranchViewSet,basename='Branch')

urlpatterns = [
    path('',include(router.urls))
]
