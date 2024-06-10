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
from adminapp.serializers import *
            
            
class EventView(ViewSet):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    
    def create(self,request,*args,**kwargs):
        serializer=EventSerializer(data=request.data)
        user_id=request.user
        if user_id.is_superuser:
            if serializer.is_valid():
                serializer.save(posted_by=user_id)
                return Response(data=serializer.data)
            else:
                return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'msg':"only admin can add events"},status=status.HTTP_400_BAD_REQUEST)
    
    def list(self,request,*args,**kwargs):
        qs=Event.objects.all()
        serializer=EventSerializer(qs,many=True)
        return Response(data=serializer.data)
    
    def retrieve(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Event.objects.get(id=id)
        serializer=EventSerializer(qs)
        return Response(data=serializer.data)
    
    def destroy(self, request, *args, **kwargs):
        id = kwargs.get("pk")
        try:
            instance =Event.objects.get(id=id)
            instance.delete()
            return Response({"msg": "Event removed"})
        except Event.DoesNotExist:
            return Response({"msg": "Event not found"}, status=status.HTTP_404_NOT_FOUND)
        
        

class StudentsView(ViewSet):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    
    
    def list(self,request,*args,**kwargs):
        qs=CustomUser.objects.filter(is_student=True)
        serializer=UserSerializer(qs,many=True)
        return Response(data=serializer.data)
    
    
    def retrieve(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=CustomUser.objects.get(id=id)
        detail_qs=StudentProfile.objects.get(user=id)
        student_serializer=UserSerializer(qs)
        student_detail=StudentProfileSerializer(detail_qs)
        student_detailserializer=student_detail.data
        response_data={
            "student":student_serializer.data,
            "student_detail":student_detailserializer
        }
        return Response(data=response_data)      


class CollegeView(ViewSet):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    
    def list(self,request,*args,**kwargs):
        qs=CustomUser.objects.filter(is_college=True)
        serializer=CollegeSerializer(qs,many=True)
        return Response(data=serializer.data)
    
    def retrieve(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=CustomUser.objects.get(id=id)
        serializer=CollegeSerializer(qs)
        return Response(data=serializer.data) 
    

class SponsorView(ViewSet):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    
    
    def list(self,request,*args,**kwargs):
        qs=CustomUser.objects.filter(is_sponsor=True,is_adminapproved=False)
        serializer=SponsorsSerializer(qs,many=True)
        return Response(data=serializer.data)
    
    def retrieve(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=CustomUser.objects.get(id=id)
        serializer=SponsorsSerializer(qs)
        return Response(data=serializer.data) 
    
    @action(methods=['post'],detail=True)
    def approve_sponsor(self, request, *args, **kwargs):
        sponsor_id = kwargs.get("pk")
        sponsor_obj = CustomUser.objects.get(id=sponsor_id)
        sponsor_obj.is_adminapproved = True
        sponsor_obj.save()
        return Response({'msg':"admin approval success"})
    
    
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
    