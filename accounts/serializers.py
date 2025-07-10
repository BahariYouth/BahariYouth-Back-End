from rest_framework import serializers
from .models import User
from django.contrib.auth.password_validation import validate_password
from structure.serializers import GovernorateSerializers,CentralUnitSerializers

class UserSerializers(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()
    governorate = GovernorateSerializers()
    central_unit = CentralUnitSerializers()
    class Meta:
        model = User
        fields = [
            'id', 
            'email', 
            'full_name', 
            'password', 
            'image_url',
            'role',
            'governorate', 
            'central_unit',
        ]
        extra_kwargs = {
            'password': {'write_only': True},
            'image': {'required': False}
        }
        
    def get_image_url(self, obj):
        if obj.image:
            return obj.image.build_url()
        return None


class UserSignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, validators=[validate_password])
    image = serializers.ImageField(required=False)

    class Meta:
        model = User
        fields = ['email', 'full_name','password','image']
    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user
    

class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)