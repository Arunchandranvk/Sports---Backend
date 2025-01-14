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
from .serializers import *
from athleteapp.models import ParticipateEvent
from athleteapp.serializers import ParticipateeventSer


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
        print(clg_id)
        qs=CustomUser.objects.get(id=clg_id)
        name=request.data.get('first_name')
        username = request.data.get('username')
        password = request.data.get('password')
        user_email = request.data.get('email')
        serializer=StudentRegistrationSerializer(data=request.data)
      
        if serializer.is_valid():
            print("valid")
            serializer.save(college_id=qs,is_student=True)
            
            subject = "Sports management Registration!"
            message = (
                f"Dear {name},\n\n"
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
        students_qs = CustomUser.objects.filter(is_student=True, college_id=clg_id)
        stu_qs = StudentProfile.objects.filter(user__in=students_qs)
        print(stu_qs)
        serializer=StudentListSerializer1(stu_qs,many=True)
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
        qs=Sponsorship.objects.filter(student__user__college_id=clg_id,is_collegeapproved="Waiting")
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
        sponsor_obj.is_collegeapproved="Accept"
        sponsor_obj.save()
        serializer=SponsorshipSerializer(sponsor_obj)
        return Response({"msg":"sponsorship has been approved","data":serializer.data})
    
    @action(methods=["post"],detail=True)
    def reject_sponsor(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        sponsor_obj=Sponsorship.objects.get(id=id)
        sponsor_obj.is_collegeapproved="Reject"
        sponsor_obj.save()
        serializer=SponsorshipSerializer(sponsor_obj)
        return Response({"msg":"sponsorship has been Rejecetd","data":serializer.data})
    
    
class EventParticipatedStudentsView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        user = request.user
        stuu = []
        students = CustomUser.objects.filter(college_id=user.username)
        for stu in students:
            events = ParticipateEvent.objects.filter(student=stu.id)
            if events.exists():
                stuu.extend(events)
        if not stuu:
            return Response("No Events Registered!!!!!!", status=status.HTTP_200_OK)
        ser = ParticipateeventSer(stuu, many=True)
        return Response(data=ser.data, status=status.HTTP_200_OK)

class SponsorshipStuView(ViewSet):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    
    def list(self,request,*args,**kwargs):
        clg_id=request.user
        qs=Sponsorship.objects.filter(student__user__college_id=clg_id,is_collegeapproved="Accept")
        serializer=SponsorshipSerializer1(qs,many=True)
        return Response(data=serializer.data)
    