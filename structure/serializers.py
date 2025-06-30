from rest_framework import serializers
from .models import Governorate,Department,Branch

class GovernorateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Governorate
        fields = '__all__'


class DepartmentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'


class BranchSerializers(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = '__all__'
        