from adminapp import models 
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from adminapp.models import *
from .models import *

class ParticipateeventSer(serializers.ModelSerializer):
    event_name = serializers.ReadOnlyField(source='event.title')
    student_name = serializers.SerializerMethodField()
    class Meta:
        model=ParticipateEvent
        fields=['id','event','student_name','event_name']
    def get_student_name(self, obj):
        try:
            print("good")
            student_profile = obj.student.id  
            print(student_profile)
            stu=StudentProfile.objects.get(user=student_profile)
            print("student",stu)
            return stu.name if stu else None
        except:
            pass
    
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
        
class WinnerSerializerget(serializers.ModelSerializer):

    event_name = serializers.ReadOnlyField(source='event.title')
    class Meta:
        model=Winner 
        fields=['event_name','event','position']
        
        
class ProfileSerializer(serializers.ModelSerializer):
    user=serializers.CharField(read_only=True)
    class Meta:
        model=StudentProfile
        fields="__all__"
        
class ProfileEditSerializer(serializers.ModelSerializer):
    class Meta:
        model=StudentProfile
        fields=["name","adm_no","age","ph_no","photo",'dob','bankname','accno','ifsc_code','achivements','interest']
        
        
class SponsorshipSerializer(serializers.ModelSerializer):
    sponsor=serializers.CharField(read_only=True)
    student=serializers.CharField(read_only=True)
    class Meta:
        model=Sponsorship
        fields="__all__"