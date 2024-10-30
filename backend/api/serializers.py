from django.contrib.auth.models import User
from rest_framework import serializers
from django.utils import timezone

        
class UserSerializer(serializers.ModelSerializer):
    createdAt = serializers.DateTimeField(default=timezone.now, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'createdAt']
        extra_kwargs = {
            'email': {'write_only': True},
            'password': {'write_only': True}
        }
    
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user