from django.shortcuts import render
from project.viewsets import BahariYouthViewset
from .models import Governorate
from .serializers import GovernorateSerializers



class GovernorateViewSet(BahariYouthViewset):
    queryset = Governorate.objects.all()
    serializer_class = GovernorateSerializers
    
