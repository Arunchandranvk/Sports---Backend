from adminapp import models 
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from adminapp.models import *


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        if username and password:
            user = authenticate(username=username, password=password)

            if not user:
                msg = 'Unable to log in with provided credentials.'
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = 'Must include "username" and "password".'
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs
    
    
class EventSerializer(serializers.ModelSerializer):
    posted_by=serializers.CharField(read_only=True)
    class Meta:
        model=Event
        fields="__all__"
        

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=CustomUser
        fields=["id","username","email","profile_picture","date_joined"]
        

class StudentProfileSerializer(serializers.ModelSerializer):
    user=serializers.CharField(read_only=True)
    event=serializers.CharField(read_only=True)
    class Meta:
        model=StudentProfile
        fields="__all__"
        
        
class SponsorsSerializer(serializers.ModelSerializer):
    class Meta:
        model=CustomUser
        fields=["id","username","email","profile_picture","date_joined","is_adminapproved"]    
        
        
class CollegeSerializer(serializers.ModelSerializer):
    class Meta:
        model=CustomUser
        fields=["id","first_name","username","email","profile_picture","date_joined"]      
        
        
class WinnerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Winner
        fields="__all__"