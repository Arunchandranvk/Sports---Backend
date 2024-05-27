from adminapp import models 
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from adminapp.models import *

    
    
class EventSerializer(serializers.ModelSerializer):
    posted_by=serializers.CharField(read_only=True)
    class Meta:
        model=Event
        fields="__all__"
        

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=CustomUser
        fields="__all__"
        
        
class WinnerSerializer(serializers.ModelSerializer):
    event=serializers.CharField(read_only=True)
    student=serializers.CharField(read_only=True)
    class Meta:
        model=Winner
        fields="__all__"
        
        
class ProfileSerializer(serializers.ModelSerializer):
    user=serializers.CharField(read_only=True)
    event=serializers.CharField(read_only=True)
    class Meta:
        model=StudentProfile
        fields="__all__"
        
        
class SponsorshipSerializer(serializers.ModelSerializer):
    sponsor=serializers.CharField(read_only=True)
    student=serializers.CharField(read_only=True)
    class Meta:
        model=Sponsorship
        fields="__all__"