from rest_framework import serializers
from .models import Activities
from structure.serializers import GovernorateSerializers
from accounts.serializers import UserSerializers


class ActivitySerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    governorate = GovernorateSerializers()
    created_by = UserSerializers()
    updated_by = UserSerializers()
    class Meta:
        model = Activities
        fields = [
            'title_ar',
            'title_en',
            'description_ar',
            'description_en',
            'address_ar',
            'address_en',
            'date',
            'image',
            'category',
            'tickets',
            'status',
            'is_private',
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