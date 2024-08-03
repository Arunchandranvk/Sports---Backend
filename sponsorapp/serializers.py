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
        

class StudentSerializer(serializers.ModelSerializer):
    college_id=serializers.CharField(read_only=True)
    class Meta:
        model=CustomUser
        fields=["id","first_name","email","college_id"]
        

class StudentDetailSerializer(serializers.ModelSerializer):
    user=serializers.CharField(read_only=True)
    event=serializers.CharField(read_only=True)
    class Meta:
        model=StudentProfile
        fields="__all__"

        
# class WinnerSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=Winner
#         fields="__all__"
        
        
class SponsorshipSerializer(serializers.ModelSerializer):
    class Meta:
        model=Sponsorship
        fields=["note","payment"]
        
class SponsorshipListSerializer(serializers.ModelSerializer):
    student=serializers.CharField(read_only=True)
    student_clg = serializers.SerializerMethodField()
    class Meta:
        model=Sponsorship
        fields=["student","student_clg","note","payment","is_collegeapproved"]
        
    def get_student_clg(self, obj):
        try:
            student_profile = obj.student.user.college_id  # Access the related StudentProfile through user
            # clg=CustomUser.objects.get(username=student_profile)
            return student_profile if student_profile else None
        except:
            pass