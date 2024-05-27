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


class StudentRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password','is_college','is_sponsor','is_student','profile_picture','first_name']
        

class StudentDetailSerializer(serializers.ModelSerializer):
    user=serializers.CharField(read_only=True)
    event=serializers.CharField(read_only=True)
    class Meta:
        model=StudentProfile
        fields="__all__"

        
class WinnerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Winner
        fields="__all__"
        
        
class SponsorshipSerializer(serializers.ModelSerializer):
    class Meta:
        model=Sponsorship
        fields="__all__"