from adminapp import models 
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
# Create your views here.

class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = models.CustomUser
        fields = ['username', 'email', 'password','is_college','is_sponsor','is_student','profile_picture','first_name']

    def create(self, validated_data):
        user = models.CustomUser.objects.create_user(**validated_data)
        return user
