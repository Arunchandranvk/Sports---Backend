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
from sponsorapp.serializers import *


class profileView(APIView):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    
    def get(self,request,*args,**kwargs):
        emp_id=request.user.id
        qs=CustomUser.objects.get(id=emp_id)
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
        
        

class StudentsView(ViewSet):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    
    
    def list(self,request,*args,**kwargs):
        qs=CustomUser.objects.filter(is_student=True)
        serializer=StudentSerializer(qs,many=True)
        return Response(data=serializer.data)
    
    def retrieve(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=CustomUser.objects.get(id=id)
        serializer=StudentSerializer(qs)
        return Response(data=serializer.data)
    
    @action(methods=["post"],detail=True)
    def sponsor_child(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=CustomUser.objects.get(id=id) 


class CollegeView(ViewSet):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    
    
    def list(self,request,*args,**kwargs):
        qs=CustomUser.objects.filter(is_college=True)
        serializer=UserSerializer(qs,many=True)
        return Response(data=serializer.data)
    
    def retrieve(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=CustomUser.objects.get(id=id)
        serializer=UserSerializer(qs)
        return Response(data=serializer.data) 

    
    
class WinnerView(ViewSet):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    
    
    def list(self,request,*args,**kwargs):
        qs=Winner.objects.all()
        serializer=WinnerSerializer(qs,many=True)
        return Response(data=serializer.data)
    
    def retrieve(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Winner.objects.get(id=id)
        serializer=WinnerSerializer(qs)
        return Response(data=serializer.data) 
    
    
    
class MysponsorshipView(ViewSet):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    
    
    def list(self,request,*args,**kwargs):
        emp_id=request.user.id
        emp_obj=CustomUser.objects.get(id=emp_id)
        qs=Sponsorship.objects.filter(sponsor=emp_obj)
        serializer=SponsorshipSerializer(qs,many=True)
        return Response(data=serializer.data)
    
    def retrieve(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Sponsorship.objects.get(id=id)
        serializer=SponsorshipSerializer(qs)
        return Response(data=serializer.data) 
    