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
    email_name=serializers.ReadOnlyField(source="user.email")
    class Meta:
        model=StudentProfile
        fields=['id','name','user','event','age','ph_no','adm_no','photo','dob','achivements','interest','email_name','bankname','accno','ifsc_code']

class SponsorShipSerializer(serializers.ModelSerializer):
    student_name = serializers.SerializerMethodField()

    class Meta:
        model = Sponsorship
        fields = ['id', 'sponsor', 'student_name', 'note', 'payment']

    def get_student_name(self, obj):
        try:
            # Assumes `obj` is an instance of Sponsorship and has a related StudentProfile
            student_profile = obj.student  # Access the related StudentProfile through user
            return student_profile.name if student_profile else None
        except:
            pass
        
       
        
class SponsorsSerializer(serializers.ModelSerializer):
    class Meta:
        model=CustomUser
        fields=["id","username","email","profile_picture","date_joined","is_adminapproved"]    
        
        
class CollegeSerializer(serializers.ModelSerializer):
    class Meta:
        model=CustomUser
        fields=["id","first_name","username","email","profile_picture","date_joined"]      
        
        
class WinnerSerializer(serializers.ModelSerializer):
    event_name = serializers.ReadOnlyField(source='event.title')
    student_name =serializers.ReadOnlyField(source='student.name')
    student_clg = serializers.SerializerMethodField()
    class Meta:
        model=Winner
        fields=['event','position','student_name','level','event_name','student','student_clg']
        
    def get_student_clg(self, obj):
        try:
            student_profile = obj.student.user.college_id  # Access the related StudentProfile through user
            # clg=CustomUser.objects.get(username=student_profile)
            return student_profile if student_profile else None
        except:
            pass
 
        
class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'