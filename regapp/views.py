from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import authentication
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet,ViewSet
from rest_framework import status
from rest_framework.decorators import action
from django.db.models import Count, Sum, F, ExpressionWrapper, FloatField

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token


from adminapp.models import *
from regapp.serializers import *
from django.utils import timezone
from datetime import timedelta




class RegistrationView(APIView):
    def post(self,request,*args,**kwargs):
        serializer=RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data={"msg": "Registration success","data":serializer.data})
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class LoginView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        
        if user:
            # Calculate the time window for notification (2 days from now)
            now = timezone.now()
            upcoming_due_date = now + timedelta(days=2)
            
            # Find events that are due within the next 2 days
            events = Event.objects.filter(due_date__date__range=[now.date(), upcoming_due_date.date()])
            
            for event in events:
                message = (
                    f"The event '{event.title}' is due in {event.due_date - now}.\n"
                    # f"Details:\n"
                    # f"Title: {event.title}\n"
                    # f"Venue: {event.venue}\n"
                    # f"Description: {event.description}\n"
                )
                Notification.objects.create(
                    user=event.posted_by,
                    event=event,
                    message=message
                )
                print(f"Notification created for event '{event.title}' for user '{event.posted_by.username}'")

            token, created = Token.objects.get_or_create(user=user)
            return Response({
                'id': user.id,
                'token': token.key,
                'is_superuser': user.is_superuser,
                'is_student': user.is_student,
                'is_sponsor': user.is_sponsor,
                'is_college': user.is_college,
            })
        else:
            return Response(data={"msg": "Login failed"}, status=status.HTTP_403_FORBIDDEN)