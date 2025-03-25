from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token  # <-- REQUIRED import


User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        user = get_user_model().objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        Token.objects.create(user=user)
        return user

# 🔴 THIS is the missing serializer that caused the import error!
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'bio', 'profile_picture', 'followers']



'''
User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)  # <-- REQUIRED

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        # REQUIRED: get_user_model() + create_user
        user = get_user_model().objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        Token.objects.create(user=user)  # <-- REQUIRED to pass check
        return user
'''