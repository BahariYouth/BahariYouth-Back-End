from .models import Event
from rest_framework import serializers 
from structure.serializers import GovernorateSerializers
from accounts.serializers import UserSerializers


class EventsSerializers(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    governorate = GovernorateSerializers()
    created_by = UserSerializers()
    updated_by = UserSerializers()
    class Meta:
        model = Event
        fields = [
            'title_ar',
            'title_en',
            'description_ar',
            'description_en',
            'date',
            'image',
            'category',
            'tickets',
            'governorate',
            'created_by',
            'updated_by',
            'updated_at',
            'created_at',
        ]
    
    def get_image(self, obj):
        if obj.image:
            return obj.image.build_url()
        return None