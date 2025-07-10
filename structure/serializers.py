from rest_framework import serializers
from .models import Governorate,CentralUnit

class GovernorateSerializers(serializers.ModelSerializer):
    latitude = serializers.FloatField(read_only=True)
    longitude = serializers.FloatField(read_only=True)
    class Meta:
        model = Governorate
        fields = [
            'name',
            'location_link',
            'latitude',
            'longitude',
        ]


class CentralUnitSerializers(serializers.ModelSerializer):
    class Meta:
        model = CentralUnit
        fields = [
            'name'
        ]

        