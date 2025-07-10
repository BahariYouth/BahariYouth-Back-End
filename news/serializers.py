from rest_framework import serializers
from .models import News,NewsImage
from accounts.serializers import UserSerializers
from structure.serializers import GovernorateSerializers



class NewsImageSerializers(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    class Meta:
        model = NewsImage
        fields = [
            'image'
        ]
        
    def get_image(self, obj):
        if obj.image:
            return obj.image.build_url()
        return None


class NewsSerializers(serializers.ModelSerializer):
    governorate  = GovernorateSerializers()
    created_by = UserSerializers()
    updated_by  = UserSerializers()
    images = NewsImageSerializers(many=True, read_only=True)
    class Meta:
        model = News
        fields = [
            'id',
            'title',
            'description',
            'date',
            'governorate',
            'created_by',
            'updated_by',
            'created_at',
            'updated_at',
            'images'
        ] 
    
