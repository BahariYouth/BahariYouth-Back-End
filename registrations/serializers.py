from rest_framework import serializers
from .models import RegisterationEvents,RegisterationActivities
from accounts.serializers import UserSerializers


class EventRegistrationSerializers(serializers.ModelSerializer):
    user = UserSerializers(read_only=True,many=True)
    
    class Meta:
        model = RegisterationEvents
        fields = [
            'user',
            'event'
        ]
        

class ActivitiesRegistrationSerializers(serializers.ModelSerializer):
    user = UserSerializers(read_only=True,many=True)
    
    class Meta:
        model = RegisterationActivities
        fields = [
            'user',
            'activities'
        ]


