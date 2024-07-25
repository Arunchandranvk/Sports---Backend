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
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

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
        detail_qs=StudentProfile.objects.get(user=id)
        student_serializer=StudentSerializer(qs)
        student_detail=StudentDetailSerializer(detail_qs)
        student_detailserializer=student_detail.data
        response_data={
            "student":student_serializer.data,
            "student_detail":student_detailserializer
        }
        return Response(data=response_data)
    
    @action(methods=["post"],detail=True)
    def sponsor_child(self, request, *args, **kwargs):
        serializer = SponsorshipSerializer(data=request.data)
        std_id = kwargs.get("pk")
        try:
            std_obj = CustomUser.objects.get(id=std_id)
            std_profile = StudentProfile.objects.get(user=std_obj)
            sponsor_id = request.user.id
            sponsor_obj = CustomUser.objects.get(id=sponsor_id)
            if serializer.is_valid():
                sponsorship = serializer.save(sponsor=sponsor_obj, student=std_profile)
                # Send email
                subject = "Sponsorship Approved"
                student_name = std_obj.get_full_name()
                amount = sponsorship.payment  # Adjust based on your model
                recipient_email = std_obj.email
                # Render the email content
                email_content = render_to_string('sponsor.html', {
                    'student_name': student_name,
                    'amount': amount,
                })
                send_mail(
                    subject,
                    f"Congratulations {student_name}! Your Sponsorship of ${amount} is Approved",
                    settings.DEFAULT_FROM_EMAIL,
                    [recipient_email],
                    html_message=email_content
                )
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except CustomUser.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        except StudentProfile.DoesNotExist:
            return Response({'error': 'Student profile not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        


class CollegeView(ViewSet):
    # authentication_classes=[authentication.TokenAuthentication]
    # permission_classes=[permissions.IsAuthenticated]
    
    
    def list(self,request,*args,**kwargs):
        qs=CustomUser.objects.filter(is_college=True)
        serializer=UserSerializer(qs,many=True)
        return Response(data=serializer.data)
    
    def retrieve(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=CustomUser.objects.get(id=id)
        stu=StudentProfile.objects.filter(user=qs)
        serializer=StudentDetailSerializer(stu,many=True)
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
        serializer=SponsorshipListSerializer(qs,many=True)
        return Response(data=serializer.data)
    
    def retrieve(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Sponsorship.objects.get(id=id)
        serializer=SponsorshipListSerializer(qs)
        return Response(data=serializer.data) 
    