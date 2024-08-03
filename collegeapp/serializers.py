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
        

class StudentListSerializer(serializers.ModelSerializer):

    class Meta:
        model=CustomUser
        fields=["id","email","first_name","profile_picture","username","password"]

    

class StudentListSerializer1(serializers.ModelSerializer):
    email_name=serializers.SerializerMethodField()
    # first_name=serializers.SerializerMethodField()
    class Meta:
        model=StudentProfile
        fields=["id",'user',"email_name","name",'photo']

    def get_email_name(self, obj):
        try:
            student_profile = obj.user
            print("stu",student_profile)
            
            return student_profile.email if student_profile else None
        except:
            pass
   
    
    
class StudentRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password','is_college','is_sponsor','is_student','first_name']
    
    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user    

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
    sponsor_name = serializers.SerializerMethodField()
    sponsor_email = serializers.SerializerMethodField()
    student_name = serializers.SerializerMethodField()

    class Meta:
        model = Sponsorship
        fields = ['id','student_name', 'sponsor_name', 'sponsor_email']
  
    def get_student_name(self, obj):
        try:
            student_profile = obj.student  # Access the related StudentProfile through the 'student' field
            return student_profile.name if student_profile else None
        except:
            pass
    def get_sponsor_name(self, obj):
        try:
            student_profile = obj.sponsor  # Access the related StudentProfile through the 'student' field
            print(student_profile.username)
            return student_profile.username if student_profile else None
        except:
            pass
    def get_sponsor_email(self, obj):
        try:
            student_profile = obj.sponsor  # Access the related StudentProfile through the 'student' field
            print(student_profile.email)
            return student_profile.email if student_profile else None
        except:
            pass



class SponsorshipSerializer1(serializers.ModelSerializer):
    sponsor_name = serializers.SerializerMethodField()
    sponsor_email = serializers.SerializerMethodField()
    student_name = serializers.SerializerMethodField()

    class Meta:
        model = Sponsorship
        fields = ['id','student_name', 'sponsor_name', 'sponsor_email','note','payment']
  
    def get_student_name(self, obj):
        try:
            student_profile = obj.student  # Access the related StudentProfile through the 'student' field
            return student_profile.name if student_profile else None
        except:
            pass
    def get_sponsor_name(self, obj):
        try:
            student_profile = obj.sponsor  # Access the related StudentProfile through the 'student' field
            print(student_profile.username)
            return student_profile.username if student_profile else None
        except:
            pass
    def get_sponsor_email(self, obj):
        try:
            student_profile = obj.sponsor  # Access the related StudentProfile through the 'student' field
            print(student_profile.email)
            return student_profile.email if student_profile else None
        except:
            pass