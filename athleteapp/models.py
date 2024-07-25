from django.db import models
from adminapp.models import *
# Create your models here.


class ParticipateEvent(models.Model):
    event = models.ForeignKey(Event,on_delete=models.CASCADE,related_name='part_event')
    student=models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name='part_user',null=True)


