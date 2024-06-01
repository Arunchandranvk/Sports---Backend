from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import authentication
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet,ViewSet
from rest_framework import status
from rest_framework.decorators import action

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token

from django.core.mail import send_mail


from adminapp.models import *
from collegeapp.serializers import *


class profileView(APIView):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    
    def get(self,request,*args,**kwargs):
        clg_id=request.user.id
        qs=CustomUser.objects.get(id=clg_id)
        serializer=UserSerializer(qs)
        return Response(serializer.data)
            
            
class EventView(ViewSet):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    
    def list(self,request,*args,**kwargs):
        qs=Event.objects.all()
        serializer=EventSerializer(qs,many=True)
        return Response(data=serializer.data)
    
    def retrieve(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Event.objects.get(id=id)
        serializer=EventSerializer(qs)
        return Response(data=serializer.data)

     
class StudentRegistrationView(APIView):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    
    def post(self,request,*args,**kwargs):
        clg_id=request.user.id
        qs=CustomUser.objects.get(id=clg_id)
        username = request.data.get('username')
        password = request.data.get('password')
        user_email = request.data.get('email')
        serializer=StudentRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(college_id=qs)
            
            subject = "Sports management Registration!"
            message = (
                f"Dear User,\n\n"
                "You have been successfully registered! "
                "This email has been sent to you to confirm your registration. Your username and password are as follows:\n\n"
                f"username : {username}.\n\n"
                f"password : {password}.\n\n"
                "Best regards,\n"
                "Sports Mgmt" 
            )
            email_from = "spicesauction11@gmail.com"
            email_to = user_email
            send_mail(subject, message, email_from, [email_to])
            
            return Response(data={"msg": "Registration success","data":serializer.data})
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)       
        

class StudentsView(ViewSet):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    
    def list(self,request,*args,**kwargs):
        clg_id=request.user
        print(clg_id)
        qs=CustomUser.objects.filter(is_student=True,college_id=clg_id)
        serializer=StudentListSerializer(qs,many=True)
        return Response(data=serializer.data)
    
    def retrieve(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=CustomUser.objects.get(id=id)
        serializer=StudentListSerializer(qs)
        return Response(data=serializer.data) 
    

class SponsorshipView(ViewSet):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    
    def list(self,request,*args,**kwargs):
        clg_id=request.user
        qs=Sponsorship.objects.filter(student__user__college_id=clg_id)
        serializer=SponsorshipSerializer(qs,many=True)
        return Response(data=serializer.data)
    
    def retrieve(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Sponsorship.objects.get(id=id)
        serializer=SponsorshipSerializer(qs)
        return Response(data=serializer.data)
    
    @action(methods=["post"],detail=True)
    def approve_sponsor(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        sponsor_obj=Sponsorship.objects.get(id=id)
        sponsor_obj.is_collegeapproved=True
        sponsor_obj.save()
        serializer=SponsorshipSerializer(sponsor_obj)
        return Response({"msg":"sponsorship has been approved","data":serializer.data})