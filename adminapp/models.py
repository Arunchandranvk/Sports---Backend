from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator,MaxValueValidator
from django.db.models.signals import post_save




class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    is_student = models.BooleanField(default=False)  
    is_sponsor = models.BooleanField(default=False)
    is_college = models.BooleanField(default=False)
    is_adminapproved = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    profile_picture = models.ImageField(upload_to='images', null=True)
    college_id=models.CharField(max_length=100,null=True)


class Event(models.Model):
    posted_by=models.ForeignKey(CustomUser,on_delete=models.CASCADE,default=None,blank=True)
    title = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    due_date=models.DateTimeField(null=True)
    venue = models.TextField()
    description = models.TextField()
    image=models.ImageField(null=True)
    def __str__(self):
        return self.title

class StudentProfile(models.Model):
   user=models.OneToOneField(CustomUser,on_delete=models.CASCADE,related_name='student_profile')
   name = models.CharField(max_length=100,null=True)
   age=models.PositiveIntegerField(null=True)
   ph_no=models.PositiveIntegerField(null=True)
   adm_no = models.PositiveIntegerField(null=True)
   photo=models.ImageField(upload_to="student profile",null=True)
   dob=models.CharField(max_length=100,null=True)

   #bank details
   bankname=models.CharField(max_length=100,null=True)
   accno=models.IntegerField(null=True)
   ifsc_code=models.CharField(max_length=100,null=True)


   def __str__(self):
        return self.name if self.name else "Unnamed Student"


class Sponsorship(models.Model):
    sponsor=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    student=models.ForeignKey(StudentProfile,on_delete=models.CASCADE)
    note=models.CharField(max_length=100)
    payment=models.IntegerField(null=True,blank=True)
    is_collegeapproved=models.BooleanField(default=False)
    
    def __str__(self):
        return str(self.sponsor)  
    
    
class Complaints(models.Model):
    user=models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    note=models.CharField(max_length=100)
    action_taken=models.BooleanField(default=False) 
    

class Winner(models.Model):
    event=models.ForeignKey(Event,on_delete=models.CASCADE)
    student=models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    position=models.PositiveIntegerField(validators=[MinValueValidator(1),MaxValueValidator(3)])
    
    
class Feedback(models.Model):
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE)    
    event=models.ForeignKey(Event, on_delete=models.CASCADE)
    rating=models.PositiveIntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    comment=models.CharField(max_length=100)
    
    
def create_profile(sender,created,instance,**kwargs):
    if created:
        if instance.is_student:
            StudentProfile.objects.create(user=instance)
        else:
            return None



post_save.connect(create_profile,sender=CustomUser)