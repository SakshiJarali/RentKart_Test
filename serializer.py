from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    phone = serializers.CharField(max_length=10)
    created_at = serializers.DateTimeField(read_only=True)  # Mark it as read-only

    class Meta:
        model = User
        fields = '__all__'
