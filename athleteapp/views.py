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

from adminapp.models import *
from athleteapp.serializers import *
            
            
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
        
      

class profileView(APIView):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    
    def get(self,request,*args,**kwargs):
        emp_id=request.user.id
        emp_obj=CustomUser.objects.get(id=emp_id)
        qs=StudentProfile.objects.get(user=emp_obj)
        serializer=ProfileSerializer(qs)
        return Response(serializer.data)
         
    

class SponsorshipView(ViewSet):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    
    
    def list(self,request,*args,**kwargs):
        emp_id=request.user.id
        emp_obj=CustomUser.objects.get(id=emp_id)
        stud_id=StudentProfile.objects.get(user=emp_obj)
        qs=Sponsorship.objects.filter(student=stud_id)
        serializer=SponsorshipSerializer(qs,many=True)
        return Response(data=serializer.data)
    
    def retrieve(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Sponsorship.objects.get(id=id)
        serializer=SponsorshipSerializer(qs)
        return Response(data=serializer.data) 
    
    
class WinnerView(ViewSet):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    
    
    def list(self,request,*args,**kwargs):
        emp_id=request.user.id
        emp_obj=CustomUser.objects.get(id=emp_id)
        qs=Winner.objects.filter(student=emp_obj)
        serializer=WinnerSerializer(qs,many=True)
        return Response(data=serializer.data)
    
    def retrieve(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Winner.objects.get(id=id)
        serializer=WinnerSerializer(qs)
        return Response(data=serializer.data) 
    