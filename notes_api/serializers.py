from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)  # Hide password in response

    class Meta:
        model = User
        fields = ('id', 'username', 'password') 