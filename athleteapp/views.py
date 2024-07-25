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
    
    
    def put(self, request, *args, **kwargs): 
        emp_id = request.user.id
        emp_obj = CustomUser.objects.get(id=emp_id)
        profile_obj = StudentProfile.objects.get(user=emp_obj) 
        serializer = ProfileEditSerializer(instance=profile_obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        

    

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


class ParticipateEventView(APIView):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    # def post(self,request):
    #     us=self.request.user.id
    #     print(us)
    #     user=CustomUser.objects.get(id=us)
    #     print(user)
    #     ser=ParticipateeventSer(data=request.POST)
    #     if ser.is_valid():
    #         ser.save(student=user)
    #         return Response(ser.data,status=status.HTTP_201_CREATED)
    #     else:
    #         return Response(status=status.HTTP_400_BAD_REQUEST)
    def get(self,request,event_id):
        us=self.request.user.id
        print(us)

        try:
            envt = Event.objects.get(id=event_id)
            user=CustomUser.objects.get(id=us)
            ParticipateEvent.objects.create(event=envt,student=user)
            events=ParticipateEvent.objects.filter(student=user)
            print(events)
            ser=ParticipateeventSer(events,many=True)
            return Response(ser.data)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)



            


class ParticipateEventViewGET(APIView):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    def get(self,request):
        us=self.request.user.id
        print(us)

        try:
            user=CustomUser.objects.get(id=us)
            events=ParticipateEvent.objects.filter(student=user)
            print(events)
            ser=ParticipateeventSer(events,many=True)
            return Response(ser.data)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class MyWins(APIView):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    def get(self,request):
        us=self.request.user.id
        print(us)
        try:
            user=CustomUser.objects.get(id=us)
            wins=Winner.objects.filter(student=user)
            ser=WinnerSerializerget(wins,many=True)
            return Response(ser.data)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)