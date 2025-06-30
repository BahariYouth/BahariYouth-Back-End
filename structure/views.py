from django.shortcuts import render
from project.viewsets import BahariYouthViewset
from .models import Branch,Governorate,Department
from .serializers import GovernorateSerializers,DepartmentSerializers,BranchSerializers



class GovernorateViewSet(BahariYouthViewset):
    queryset = Governorate.objects.all()
    serializer_class = GovernorateSerializers
    
    
class DepartmentViewSet(BahariYouthViewset):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializers


class BranchViewSet(BahariYouthViewset):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializers
